import {
  AppShell,
  Container,
  Group,
} from "@mantine/core";
import { createBrowserRouter, RouterProvider, Outlet, useLocation } from "react-router-dom";
import { useEffect } from "react";

import Home from "./pages/Home";
import Book from "./pages/Book";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Search from "./pages/Search";
import Nav from "./components/Structure/Nav";
import Footer from "./components/Structure/Footer";
import PageNotFound from "./pages/PageNotFound";
import UserProfile from "./pages/UserProfile";
import PrivateRoute from "./components/Structure/PrivateRoute";

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
      {
        path: "/me",
        element: <PrivateRoute><UserProfile /></PrivateRoute>,
      },
      {
        path: "*",
        element: <PageNotFound />,
      }
    ],
  },
]);

function SiteShell() {
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location.pathname]);

  return (
    <AppShell
      header={{ height: 80 }}
      padding="md"
    >
      <AppShell.Header style={{ width: "100%" }}>
        <Group w="100%" h="100%" px="md" style={{ 
          background: 'linear-gradient(to bottom, var(--mantine-color-dark-0), var(--mantine-color-dark-9))'
        }}>
          <Nav />
        </Group>
      </AppShell.Header>
      <AppShell.Main style={{ 
        background: 'linear-gradient(to right, var(--mantine-color-teal-5), var(--mantine-color-teal-2), var(--mantine-color-teal-0), var(--mantine-color-teal-2), var(--mantine-color-teal-5))'
      }}>
        {/* Note: Container is used to center the content and limit the width */}
        <Container size="sm">
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
