import { AppShell, Container, Group } from "@mantine/core";
import {
  createBrowserRouter,
  RouterProvider,
  Outlet,
  useNavigate,
  useLocation,
} from "react-router-dom";
import { useEffect } from "react";

import Home from "./pages/Home";
import Book from "./pages/Book";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Search from "./pages/Search";
import Nav from "./components/Structure/Nav";
import Footer from "./components/Structure/Footer";
import BadReadLogo from "./components/BadReadLogo";
import { useMediaQuery } from "@mantine/hooks";
import PageNotFound from "./pages/PageNotFound";
import UserProfile from "./pages/UserProfile";
import PrivateRoute from "./components/Structure/PrivateRoute";
import BookClub from "./pages/BookClub";
import BookClubHome from "./pages/BookClubHome";

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
        element: (
          <PrivateRoute>
            <UserProfile />
          </PrivateRoute>
        ),
      },
      {
        path: "*",
        element: <PageNotFound />,
      },
      {
        path: "/book-clubs",
        element: <BookClubHome />,
      },
      {
        path: "/book-club/:id",
        element: <BookClub />,
      },
    ],
  },
]);

function SiteShell() {
  // const [opened, { toggle }] = useDisclosure();
  const isCompact = useMediaQuery("(max-width: 560px)");

  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location.pathname]);

  return (
    <AppShell
      header={{ height: 80 }}
      padding="md"
      // navbar={{
      //   width: 200,
      //   breakpoint: "xs",
      //   collapsed: { desktop: false, mobile: opened },
      // }}
    >
      <AppShell.Header>
        {/* <Burger opened={opened} onClick={toggle} hiddenFrom="xs" size="xs" /> */}
        <Group
          px="md"
          style={{
            background:
              "linear-gradient(to bottom, var(--mantine-color-dark-0), var(--mantine-color-dark-9))",
          }}
        >
          <Group justify="space-between" style={{ flex: 1 }}>
            {!isCompact && (
              <Group
                onClick={() => navigate("/")}
                style={{ cursor: "pointer" }}
              >
                <BadReadLogo />
                <h1 style={{ color: "white" }}>Bad Reads</h1>
              </Group>
            )}
            <Group gap={0}>
              <Nav />
            </Group>
          </Group>
        </Group>
      </AppShell.Header>

      {/* <AppShell.Navbar py="md" px={4}>
        <Burger opened={opened} onClick={toggle} hiddenFrom="xs" size="xs" />
        <Nav />
      </AppShell.Navbar> */}

      <AppShell.Main
        style={{
          background:
            "linear-gradient(to right, var(--mantine-color-teal-5), var(--mantine-color-teal-2), var(--mantine-color-teal-0), var(--mantine-color-teal-2), var(--mantine-color-teal-5))",
          margin: "auto 0",
        }}
      >
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
