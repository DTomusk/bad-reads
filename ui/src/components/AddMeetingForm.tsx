import {
  Button,
  Group,
  SimpleGrid,
  Stack,
  Textarea,
  TextInput,
  Title,
  Text,
} from "@mantine/core";
import { DatePicker } from "@mantine/dates";

import { useForm } from "@mantine/form";

export function AddMeetingForm() {
  const form = useForm({
    initialValues: {
      book: "",
      date: "",
      meetingLead: "",
    },
    validate: {
      book: (value) => value.trim().length < 2,
      date: (value) => !/^\S+@\S+$/.test(value),
      meetingLead: (value) => value.trim().length === 0,
    },
  });

  return (
    <form
      onSubmit={form.onSubmit(() => {})}
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center", // center horizontally
        width: "100%",
        maxWidth: 400,
      }}
    >
      <Title
        order={2}
        size="h1"
        fw={900}
        ta="center"
        c="black"
        style={{ fontFamily: "Outfit, var(--mantine-font-family)" }}
      >
        Add New Meeting
      </Title>
      <TextInput
        label="Book Chooser"
        placeholder="Book Chooser"
        mt="md"
        name="meetingLead"
        variant="filled"
        withAsterisk
        width="100%"
        c="black"
        {...form.getInputProps("meetingLead")}
      />
      <TextInput
        label="Book"
        placeholder="Chosen Book"
        name="name"
        variant="filled"
        withAsterisk
        c="black"
        {...form.getInputProps("book")}
      />
      <Text mt="sm" ta="center" c="dimmed">
        {" "}
        Meeting Date
      </Text>
      <DatePicker
        {...form.getInputProps("date")}
        style={{ justifyItems: "center" }}
      />

      <Group justify="center" mt="xl">
        <Button type="submit" size="md">
          Create Meeting
        </Button>
      </Group>
    </form>
  );
}
