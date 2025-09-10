import { Stack, Title, Text, Button } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthProvider"; 
import BookRow from "../components/Books/BookRow";
import { useBooks } from "../hooks/useBooks";

export default function Home() {
  const navigate = useNavigate();
  const { isAuthenticated, user } = useAuth();
  const { data: books } = useBooks();
  return (
    <Stack>
      <Stack gap="lg" mt="5rem" align="center" mb="5rem"> 
        {!isAuthenticated && <><Text
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
            fontSize: "64px"
          }}
          c="white"
        >
          💩Bad Reads💖
        </Title></>}
        {isAuthenticated && <><Text
          style={{
            alignSelf: "center",
            fontSize: "var(--mantine-font-size-xl)",
          }}
          c="white"
        >
          Welcome back
        </Text>
        <Title
          order={1}
          style={{
            alignSelf: "center",
            fontSize: "64px"
          }}
          c="white"
        >
          💩{user?.username}💖
        </Title></>}
        {!isAuthenticated && <Text
          style={{
            alignSelf: "center",
            fontSize: "var(--mantine-font-size-xl)",
          }}
          c="white"
        >
          Because even bad books can be great
        </Text>}
        {isAuthenticated && <Text
          style={{
            alignSelf: "center",
            fontSize: "var(--mantine-font-size-xl)",
          }}
          c="white"
        >
          Show us how bad your taste really is
        </Text>}
        {!isAuthenticated && <Button w="auto" size="md" mt="lg" onClick={() => navigate("/register")}>Register now and start rating!</Button>}
      </Stack>
      {isAuthenticated && <BookRow books={books || []} />}
    </Stack>
  );
}
