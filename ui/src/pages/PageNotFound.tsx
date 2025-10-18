import { Stack, Text, Title } from "@mantine/core";

export default function PageNotFound() {
    return (
        <Stack style={{
            marginTop: "5rem"
        }}>
        <Title
          order={1}
          style={{
            alignSelf: "center",
            fontSize: "64px"
          }}
          c="white">404 - Page Not Found</Title>
        <Text
          style={{
            alignSelf: "center",
            fontSize: "var(--mantine-font-size-xl)",
          }}
          c="white"
        >Oopsie poopsie!</Text>
        </Stack>
    )
}