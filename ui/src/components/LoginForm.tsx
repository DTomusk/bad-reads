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

export default function LoginForm() {
  const [type, toggle] = useToggle(["login", "register"]);
  const form = useForm({
    initialValues: {
      email: "",
      name: "",
      password: "",
      terms: true,
    },

    validate: {
      email: (val) => (/^\S+@\S+$/.test(val) ? null : "Invalid email"),
      password: (val) =>
        val.length <= 6
          ? "Password should include at least 6 characters"
          : null,
    },
  });
  return (
    <form onSubmit={form.onSubmit(() => {})}>
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
        <Button type="submit" radius="xl" size="lg" color="orange">
          {upperFirst(type)}
        </Button>
      </Group>
    </form>
  );
}
