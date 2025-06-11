import { Center, Stack, Title, Text, Button } from "@mantine/core";

export default function Home() {
  return (
    <>
      <Center>
        <Stack gap="lg" mt="lg" align="center"> 
          <Text
            style={{
              alignSelf: "center",
              fontSize: "var(--mantine-font-size-xl)",
            }}
            c="white"
          >
            Welcome to
          </Text>
          <Title
            order={1}
            style={{
              alignSelf: "center",
              fontSize: "54px"
            }}
            c="white"
          >
            💩Bad Reads💖
          </Title>
          <Text
            style={{
              alignSelf: "center",
              fontSize: "var(--mantine-font-size-xl)",
            }}
            c="white"
          >
            Because even bad books can be great
          </Text>
          <Button w="auto" size="md" mt="lg">Register and start rating!</Button>
        </Stack>
      </Center>
    </>
  );
}
