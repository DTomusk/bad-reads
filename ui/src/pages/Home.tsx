import { Autocomplete, Center, Group, Stack, Title, Loader, Text } from "@mantine/core";
import BookCard from "../components/BookCard";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { useQuery } from "@tanstack/react-query";
import { TBook } from "../types/book";

async function fetchBooks(): Promise<TBook[]> {
  // TODO: define base url elsewhere
  const response = await fetch('http://127.0.0.1:8000/api/books');
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
}

export default function Home() {
  const { data: books, isLoading, error } = useQuery({
    queryKey: ['books'],
    queryFn: fetchBooks
  });

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
          <Autocomplete
            placeholder="Search for bad books"
            leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
            data={[]}
            size="xl"
            visibleFrom="xs"
            style={{ alignSelf: "center", width: "50rem" }}
          />
          <Group justify="center">
            {books?.map((book) => (
              <BookCard key={book.uuid} {...book} />
            ))}
          </Group>
        </Stack>
      </Center>
    </>
  );
}
