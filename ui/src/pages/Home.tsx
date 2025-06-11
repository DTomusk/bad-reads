import { Center, Stack, Title, Text, Button } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth"; 

export default function Home() {
  const navigate = useNavigate();
  const isLoggedIn = useAuth();
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
          {!isLoggedIn && <Button w="auto" size="md" mt="lg" onClick={() => navigate("/login")}>Register and start rating!</Button>}
        </Stack>
      </Center>
    </>
  );
}
