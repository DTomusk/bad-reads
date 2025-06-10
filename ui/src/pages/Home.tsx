import { TextInput, Center, Group, Stack, Title, Loader, Text } from "@mantine/core";
import BookCard from "../components/BookCard";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { useBooks, useBookSearch } from "../hooks/useBooks";
import { useState } from "react";

export default function Home() {
  const [searchQuery, setSearchQuery] = useState("");
  const [activeSearch, setActiveSearch] = useState("");
  const { data: books, isLoading, error } = useBooks();
  const { data: searchResults } = useBookSearch(activeSearch);

  if (isLoading) {
    return (
      <Center>
        <Loader size="xl" />
      </Center>
    );
  }

  if (error) {
    return (
      <Center>
        <Text c="red">Error loading books: {(error as Error).message}</Text>
      </Center>
    );
  }

  const displayBooks = activeSearch ? searchResults || [] : books || [];

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      setActiveSearch(searchQuery);
    }
  };

  return (
    <>
      <Center>
        <Stack>
          <Title
            style={{
              color: "var(--mantine-color-orange-filled)",
              alignSelf: "center",
            }}
          >
            Welcome to Bad Reads
          </Title>
          {/*TODO: This used to be an autocomplete, consider adding it back in*/}
          <TextInput
            placeholder="Search for bad books"
            leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
            value={searchQuery}
            onChange={(event) => setSearchQuery(event.currentTarget.value)}
            onKeyDown={handleKeyPress}
            size="xl"
            style={{ alignSelf: "center", width: "50rem" }}
          />
          <Group justify="center">
            {displayBooks.map((book) => (
              <BookCard key={book.id} {...book} />
            ))}
          </Group>
        </Stack>
      </Center>
    </>
  );
}
