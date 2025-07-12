import { Center, Stack, Title, Divider, Loader, Text } from "@mantine/core";
import BookCard from "../components/BookCard";
import { useBookSearch } from "../hooks/useBooks";
import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";

export default function Search() {
  const [searchParams] = useSearchParams();
  const [activeSearch, setActiveSearch] = useState("");
  const { data: searchResults, isLoading } = useBookSearch(activeSearch);

  useEffect(() => {
    const query = searchParams.get('q');
    if (query) {
      setActiveSearch(query);
    }
  }, [searchParams]);

  const displayBooks = searchResults || []

  return (
    <Center>
      <Stack>
        {activeSearch && (
          <Title order={2} ta="center" mb="md" mt="xl">
            Search results for "{activeSearch}"
          </Title>
        )}
        <Divider/>
        {isLoading ? (
          <Center>
            <Loader size="xl" />
          </Center>
        ) : displayBooks.length === 0 && activeSearch ? (
          <Center>
            <Text size="lg" c="dimmed" ta="center">
              No books found for "{activeSearch}"
            </Text>
          </Center>
        ) : (
          <Stack>
            {displayBooks.map((book) => (
              <>
                <BookCard key={book.id} {...book} />
                <Divider size="xs"/>
              </>
            ))}
          </Stack>
        )}
      </Stack>
    </Center>
  );
} 