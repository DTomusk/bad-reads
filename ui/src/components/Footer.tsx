import { Text, Group } from "@mantine/core";
import BadReadLogo from "./BadReadLogo";

export default function Footer() {
  return (
    <Group style={{ backgroundColor: "var(--mantine-color-orange-filled)" }}>
      <BadReadLogo color="blue" />
      <Group>
        <Text>copyright @ A really really good startup idea</Text>
      </Group>
    </Group>
  );
}
