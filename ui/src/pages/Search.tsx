import { Center, Stack, Loader, Text, Title, Divider } from "@mantine/core";
import BookCard from "../components/BookCard";
import { useBooks, useBookSearch } from "../hooks/useBooks";
import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";

export default function Search() {
  const [searchParams] = useSearchParams();
  const [activeSearch, setActiveSearch] = useState("");
  const { data: books, isLoading, error } = useBooks();
  const { data: searchResults } = useBookSearch(activeSearch);

  useEffect(() => {
    const query = searchParams.get('q');
    if (query) {
      setActiveSearch(query);
    }
  }, [searchParams]);

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

  return (
    <Center>
      <Stack>
        {activeSearch && (
          <Title order={2} ta="center" mb="md" mt="xl">
            Search results for "{activeSearch}"
          </Title>
        )}
        <Divider/>
          <Stack>
            {displayBooks.map((book) => (
              <>
                <BookCard key={book.id} {...book} />
                <Divider size="xs"/>
              </>
            ))}
          </Stack>
      </Stack>
    </Center>
  );
} 