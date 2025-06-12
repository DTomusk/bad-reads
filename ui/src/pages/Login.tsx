import {
  Stack,
  TextInput,
  PasswordInput,
  Button,
  Group,
  Anchor,
  Center,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useLogin } from "../hooks/useLogin";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();
  const { mutate: login, isPending } = useLogin();

  const form = useForm({
    initialValues: {
      email: "",
      password: "",
    },

    validate: {
      email: (val) => (/^\S+@\S+$/.test(val) ? null : "Invalid email"),
      password: (val) =>
        val.length <= 6
          ? "Password should include at least 6 characters"
          : null,
    },
  });

  const handleSubmit = (values: any) => {
    login(
      {
        username: values.email,
        password: values.password,
      },
      {
        onSuccess: (data) => {
          // Store the token in localStorage
          localStorage.setItem("token", data.access_token);
          // Redirect to home page
          navigate("/");
        },
        onError: (error) => {
          // TODO: Show error message to user
          console.error("Login failed:", error);
        },
      }
    );
  };

  return (
    <Center>
      <form onSubmit={form.onSubmit(handleSubmit)} style={{ width: "50rem", marginTop: "2rem" }}>
        <Stack>
          <TextInput
            required
            label="Email"
            placeholder="bad@bad-reads.com"
            value={form.values.email}
            onChange={(event) =>
              form.setFieldValue("email", event.currentTarget.value)
            }
            error={form.errors.email && "Invalid email"}
            radius="md"
            size="lg"
          />

          <PasswordInput
            required
            label="Password"
            placeholder="Your password"
            value={form.values.password}
            onChange={(event) =>
              form.setFieldValue("password", event.currentTarget.value)
            }
            error={
              form.errors.password &&
              "Password should include at least 6 characters"
            }
            radius="md"
            size="lg"
          />
        </Stack>

        <Group justify="space-between" mt="xl">
          <Anchor
            component="button"
            type="button"
            c="dimmed"
            onClick={() => navigate("/register")}
            size="md"
          >
            Don't have an account? Register
          </Anchor>
          <Button 
            type="submit" 
            radius="xl" 
            size="lg" 
            color="orange"
            loading={isPending}
          >
            Login
          </Button>
        </Group>
      </form>
    </Center>
  );
}
