import { Stack, Text, Textarea, Title } from "@mantine/core";

interface LimitedTextareaProps {
  title: string;
  maxLength: number;
  placeholder?: string;
  value: string;
  onChange: (value: string) => void;
  minRows?: number;
}

export default function LimitedTextarea({
  title,
  maxLength,
  placeholder,
  value,
  onChange,
  minRows = 3,
}: LimitedTextareaProps) {
  return (
    <Stack gap="xs" w="100%">
      <Title order={3} c="dark.9" mb="0">{title}</Title>
      <Text size="sm" c="dimmed" ta="right">
        {value.length}/{maxLength} characters
      </Text>
      <Textarea
        w="100%"
        bg="light"
        c="dark.9"
        placeholder={placeholder}
        value={value}
        onChange={(event) => onChange(event.currentTarget.value.slice(0, maxLength))}
        minRows={minRows}
        autosize
        maxLength={maxLength}
      />
    </Stack>
  );
} 