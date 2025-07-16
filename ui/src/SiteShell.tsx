import {
  AppShell,
  Container,
  Group,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { createBrowserRouter, RouterProvider, Outlet, useNavigate, useLocation } from "react-router-dom";
import { useEffect } from "react";

import Home from "./pages/Home";
import Book from "./pages/Book";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Search from "./pages/Search";
import Nav from "./components/Structure/Nav";
import Footer from "./components/Structure/Footer";
import BadReadLogo from "./components/BadReadLogo";

const router = createBrowserRouter([
  {
    path: "/",
    element: <SiteShell />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/book/:id",
        element: <Book />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/register",
        element: <Register />,
      },
      {
        path: "/search",
        element: <Search />,
      },
    ],
  },
]);

function SiteShell() {
  const [opened, { toggle }] = useDisclosure();
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location.pathname]);

  return (
    <AppShell
      header={{ height: 80 }}
      padding="md"
      navbar={{
        width: 300,
        breakpoint: "sm",
        collapsed: { desktop: true, mobile: !opened },
      }}
    >
      <AppShell.Header >
        <Group px="md" style={{ 
          background: 'linear-gradient(to bottom, var(--mantine-color-dark-0), var(--mantine-color-dark-9))'
        }}>
          <Group justify="space-between" style={{ flex: 1 }}>
            <Group onClick={() => navigate("/")} style={{ cursor: 'pointer' }}>
              <BadReadLogo />
              <h1 style={{ color: "white" }}>Bad Reads</h1>
            </Group>
            <Group ml="xl" gap={0} visibleFrom="sm">
              <Nav />
            </Group>
          </Group>
        </Group>
      </AppShell.Header>

      <AppShell.Navbar py="md" px={4}>
        <Nav />
      </AppShell.Navbar>

      <AppShell.Main style={{ 
        background: 'linear-gradient(to right, var(--mantine-color-teal-5), var(--mantine-color-teal-2), var(--mantine-color-teal-0), var(--mantine-color-teal-2), var(--mantine-color-teal-5))'
      }}>
        {/* Note: Container is used to center the content and limit the width */}
        <Container size="md">
          <Outlet />
        </Container>
      </AppShell.Main>
      <Footer />
    </AppShell>
  );
}

export default function App() {
  return <RouterProvider router={router} />;
}
