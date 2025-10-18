import {
  Button,
  ComboboxItem,
  Group,
  OptionsFilter,
  Select,
  Title,
} from "@mantine/core";

export function AddMemberForm() {
  const optionsFilter: OptionsFilter = ({ options, search }) => {
    const splittedSearch = search.toLowerCase().trim().split(" ");
    return (options as ComboboxItem[]).filter((option) => {
      const words = option.label.toLowerCase().trim().split(" ");
      return splittedSearch.every((searchWord) =>
        words.some((word) => word.includes(searchWord))
      );
    });
  };

  return (
    <div>
      <Title
        order={2}
        size="h1"
        fw={900}
        ta="center"
        c="black"
        style={{ fontFamily: "Outfit, var(--mantine-font-family)" }}
      >
        Add New Member
      </Title>
      <Select
        label="Your country"
        placeholder="Pick value"
        data={["Great Britain", "Russian Federation", "United States"]}
        filter={optionsFilter}
        searchable
      />

      <Group justify="center" mt="xl">
        <Button type="submit" size="md">
          Create Meeting
        </Button>
      </Group>
    </div>
  );
}
