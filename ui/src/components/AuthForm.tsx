import {
  Stack,
  TextInput,
  PasswordInput,
  Button,
  Group,
  Anchor,
  Title,
} from "@mantine/core";
import { useForm } from "@mantine/form";
import { useNavigate } from "react-router-dom";

interface FormField {
  name: string;
  label: string;
  placeholder: string;
  type: "text" | "password";
  validation?: (value: string, values?: Record<string, string>) => string | null;
}

interface AuthFormProps {
  title: string;
  fields: FormField[];
  submitLabel: string;
  alternateLabel: string;
  alternatePath: string;
  onSubmit: (values: Record<string, string>) => void;
  isPending: boolean;
}

export default function AuthForm({
  title,
  fields,
  submitLabel,
  alternateLabel,
  alternatePath,
  onSubmit,
  isPending,
}: AuthFormProps) {
  const navigate = useNavigate();

  const form = useForm({
    initialValues: fields.reduce((acc, field) => ({ ...acc, [field.name]: "" }), {} as Record<string, string>),
    validate: fields.reduce(
      (acc, field) => ({
        ...acc,
        [field.name]: field.validation || (() => null),
      }),
      {} as Record<string, (value: string, values?: Record<string, string>) => string | null>
    ),
  });

  const handleSubmit = (values: Record<string, string>) => {
    onSubmit(values);
  };

  return (
    <form onSubmit={form.onSubmit(handleSubmit)}>
      <Stack>
        <Group justify="center">
          <Title order={1} mb="xl" mt="xl">
            {title}
          </Title>
        </Group>
        {fields.map((field) => {
          const InputComponent = field.type === "password" ? PasswordInput : TextInput;
          return (
            <InputComponent
              key={field.name}
              required
              label={field.label}
              placeholder={field.placeholder}
              value={form.values[field.name]}
              onChange={(event) =>
                form.setFieldValue(field.name, event.currentTarget.value)
              }
              error={form.errors[field.name]}
              radius="md"
              size="lg"
            />
          );
        })}
      </Stack>

      <Group justify="space-between" mt="xl">
        <Anchor
          component="button"
          type="button"
          onClick={() => navigate(alternatePath)}
          size="md"
        >
          {alternateLabel}
        </Anchor>
        <Button 
          type="submit" 
          radius="xl" 
          size="lg" 
          loading={isPending}
        >
          {submitLabel}
        </Button>
      </Group>
    </form>
  );
} 