import {
  AppShell,
  Burger,
  Button,
  Center,
  Group,
  Skeleton,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Image } from "@mantine/core";

import Home from "./pages/Home";
import Book from "./pages/Book";
import Login from "./pages/Login";
import Nav from "./components/Nav";

const router = createBrowserRouter([
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
]);
export default function SiteShell() {
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
      <AppShell.Header style={{ backgroundColor: "Blue" }}>
        <Group h="100%" px="md">
          <Group justify="space-between" style={{ flex: 1 }}>
            <Image
              h={70}
              src="/bad-reads-logo.svg"
              color="orange"
              style={{ paddingBottom: "0.25rem" }}
            />

            <h1 style={{ color: "orange" }}>Bad Reads</h1>
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
        <RouterProvider router={router} />
      </AppShell.Main>
    </AppShell>
  );
}
