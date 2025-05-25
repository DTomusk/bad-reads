import {
  Anchor,
  Button,
  Center,
  Checkbox,
  Divider,
  Group,
  Paper,
  PaperProps,
  PasswordInput,
  Stack,
  Text,
  TextInput,
  Title,
} from "@mantine/core";
import LoginForm from "../components/LoginForm";

export default function LoginPage() {
  return (
    <Center>
      <Paper
        // shadow="md"
        // p="lg"
        style={{ width: "50rem", alignSelf: "center", marginTop: "2rem" }}
      >
        <Title
          order={1}
          style={{
            color: "var(--mantine-color-orange-filled)",
            textAlign: "center",
          }}
        >
          Welcome to Bad Reads
        </Title>
        <LoginForm />
      </Paper>
    </Center>
  );
}
