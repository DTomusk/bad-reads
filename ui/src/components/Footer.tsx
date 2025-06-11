import { Text, Group } from "@mantine/core";
import BadReadLogo from "./BadReadLogo";

export default function Footer() {
  return (
    <Group bg="dark.0">
      <BadReadLogo color="orange" />
      <Group>
        <Text c="white">copyright @ A really really good startup idea</Text>
      </Group>
    </Group>
  );
}
