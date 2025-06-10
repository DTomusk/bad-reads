import { Center, Stack, Title, Text } from "@mantine/core";

export default function Home() {
  return (
    <>
      <Center>
        <Stack>
          <Text
            style={{
              color: "var(--mantine-color-white)",
              alignSelf: "center",
              fontSize: "var(--mantine-font-size-xl)",
            }}
          >
            Welcome to
          </Text>
          <Title
            order={1}
            style={{
              color: "var(--mantine-color-white)",
              alignSelf: "center",
              fontSize: "54px"
            }}
          >
            💩Bad Reads💖
          </Title>
          <Text
            style={{
              color: "var(--mantine-color-white)",
              alignSelf: "center",
              fontSize: "var(--mantine-font-size-xl)",
            }}
          >
            Because even bad books can be great
          </Text>
        </Stack>
      </Center>
    </>
  );
}
