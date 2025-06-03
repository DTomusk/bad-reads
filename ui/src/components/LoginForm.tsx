import {
  Stack,
  TextInput,
  PasswordInput,
  Checkbox,
  Group,
  Anchor,
  Button,
} from "@mantine/core";

import { useForm } from "@mantine/form";
import { upperFirst, useToggle } from "@mantine/hooks";
import { useLogin } from "../hooks/useLogin";
import { useRegister } from "../hooks/useRegister";
import { useNavigate } from "react-router-dom";

// TODO: should we separate login and register?
export default function LoginForm() {
  const [type, toggle] = useToggle(["login", "register"]);
  const navigate = useNavigate();
  const { mutate: login, isPending: isLoginPending } = useLogin();
  const { mutate: register, isPending: isRegisterPending } = useRegister();

  const form = useForm({
    initialValues: {
      email: "",
      name: "",
      password: "",
      terms: true,
    },

    // TODO: match validation to backend
    validate: {
      email: (val) => (/^\S+@\S+$/.test(val) ? null : "Invalid email"),
      password: (val) =>
        val.length <= 6
          ? "Password should include at least 6 characters"
          : null,
    },
  });

  const handleSubmit = (values: any) => {
    if (type === "login") {
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
    } else {
      register(
        {
          email: values.email,
          password: values.password,
          confirm_password: values.password,
        },
        {
          onSuccess: (data) => {
            // TODO: Show success message to user, maybe a banner
            console.log("Registration successful:", data);
            toggle();
          },
          onError: (error) => {
            // TODO: Show error message to user
            console.error("Registration failed:", error);
          },
        }
      );
    }
  };

  return (
    <form onSubmit={form.onSubmit(handleSubmit)}>
      <Stack>
        {type === "register" && (
          <TextInput
            label="Name"
            placeholder="Your name"
            value={form.values.name}
            onChange={(event) =>
              form.setFieldValue("name", event.currentTarget.value)
            }
            radius="md"
            size="lg"
          />
        )}

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

        {type === "register" && (
          <Checkbox
            label="I accept terms and conditions"
            checked={form.values.terms}
            onChange={(event) =>
              form.setFieldValue("terms", event.currentTarget.checked)
            }
            size="lg"
          />
        )}
      </Stack>

      <Group justify="space-between" mt="xl">
        <Anchor
          component="button"
          type="button"
          c="dimmed"
          onClick={() => toggle()}
          size="md"
        >
          {type === "register"
            ? "Already have an account? Login"
            : "Don't have an account? Register"}
        </Anchor>
        <Button 
          type="submit" 
          radius="xl" 
          size="lg" 
          color="orange"
          loading={type === "login" ? isLoginPending : isRegisterPending}
        >
          {upperFirst(type)}
        </Button>
      </Group>
    </form>
  );
}
