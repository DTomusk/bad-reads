import { Center, Stack, Title, Text, Button } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth"; 
import BookRow from "../components/BookRow";
import { useBooks } from "../hooks/useBooks";

export default function Home() {
  const navigate = useNavigate();
  const isLoggedIn = useAuth();
  const { data: books } = useBooks();
  return (
    <>
      <Center>
        <Stack>
        <Stack gap="lg" mt="5rem" align="center" mb="5rem"> 
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
          {!isLoggedIn && <Button w="auto" size="md" mt="lg" onClick={() => navigate("/login")}>Register now and start rating!</Button>}
          
        </Stack>
        <Center>
            <BookRow books={books || []} />
          </Center>
          </Stack>
      </Center>
    </>
  );
}
