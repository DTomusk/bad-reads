import {
  AppShell,
  Group,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";

import Home from "./pages/Home";
import Book from "./pages/Book";
import Login from "./pages/Login";
import Search from "./pages/Search";
import Nav from "./components/Nav";
import Footer from "./components/Footer";
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
        path: "/search",
        element: <Search />,
      },
    ],
  },
]);

function SiteShell() {
  const [opened, { toggle }] = useDisclosure();

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
            <Group>
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

      <AppShell.Main>
        <Outlet />
      </AppShell.Main>

      <Footer />
    </AppShell>
  );
}

export default function App() {
  return <RouterProvider router={router} />;
}
