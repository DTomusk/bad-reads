import {
  Stack,
  TextInput,
  PasswordInput,
  Button,
  Group,
  Anchor,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useRegister } from "../hooks/useRegister";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const navigate = useNavigate();
  const { mutate: register, isPending } = useRegister();

  const form = useForm({
    initialValues: {
      email: "",
      password: "",
      confirm_password: "",
    },

    validate: {
      email: (val) => (/^\S+@\S+$/.test(val) ? null : "Invalid email"),
      password: (val) =>
        val.length <= 6
          ? "Password should include at least 6 characters"
          : null,
      confirm_password: (val, values) =>
        val !== values.password ? "Passwords did not match" : null,
    },
  });

  const handleSubmit = (values: any) => {
    register(
      {
        email: values.email,
        password: values.password,
        confirm_password: values.confirm_password,
      },
      {
        onSuccess: (data) => {
          // TODO: Show success message to user, maybe a banner
          console.log("Registration successful:", data);
          navigate("/login");
        },
        onError: (error) => {
          // TODO: Show error message to user
          console.error("Registration failed:", error);
        },
      }
    );
  };

  return (
    <form onSubmit={form.onSubmit(handleSubmit)}>
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

        <PasswordInput
          required
          label="Confirm Password"
          placeholder="Confirm your password"
          value={form.values.confirm_password}
          onChange={(event) =>
            form.setFieldValue("confirm_password", event.currentTarget.value)
          }
          error={form.errors.confirm_password && "Passwords did not match"}
          radius="md"
          size="lg"
        />
      </Stack>

      <Group justify="space-between" mt="xl">
        <Anchor
          component="button"
          type="button"
          c="dimmed"
          onClick={() => navigate("/login")}
          size="md"
        >
          Already have an account? Login
        </Anchor>
        <Button 
          type="submit" 
          radius="xl" 
          size="lg" 
          color="orange"
          loading={isPending}
        >
          Register
        </Button>
      </Group>
    </form>
  );
} 