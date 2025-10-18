import "@mantine/core/styles.css";
import "@mantine/dates/styles.css";

import { MantineProvider } from "@mantine/core";
import { theme } from "./theme";
import SiteShell from "./SiteShell";

export default function App() {
  return (
    <MantineProvider theme={theme}>
      <SiteShell />
    </MantineProvider>
  );
}
