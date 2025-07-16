import { Center, Stack, Title, Divider, Loader, Text, Button } from "@mantine/core";
import BookCard from "../components/BookCard";
import { useBookSearch } from "../hooks/useBooks";
import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import { TBook } from "../types/book";

export default function Search() {
  const [searchParams] = useSearchParams();
  const [activeSearch, setActiveSearch] = useState("");
  const [page, setPage] = useState(1);
  const { data: searchResults, isLoading } = useBookSearch(activeSearch, page);
  const [accumulatedBooks, setAccumulatedBooks] = useState<TBook[]>([]);

  useEffect(() => {
    const query = searchParams.get('q');
    if (query) {
      setActiveSearch(query);
      setPage(1); // Reset page when search changes
      setAccumulatedBooks([]); // Clear accumulated books for new search
    }
  }, [searchParams]);

  // Update accumulatedBooks when searchResults change
  useEffect(() => {
    if (searchResults?.books) {
      if (page === 1) {
        // For first page, replace the accumulated books
        setAccumulatedBooks(searchResults.books);
      } else {
        // For subsequent pages, append to existing books
        setAccumulatedBooks(prev => [...prev, ...searchResults.books]);
      }
    }
  }, [searchResults, page]);

  const handleLoadMore = () => {
    setPage(prev => prev + 1);
  }

  return (
    <Center w="100%">
      <Stack w="100%">
        {activeSearch && (
          <Title order={2} ta="center" mb="md" mt="xl">
            Search results for "{activeSearch}"
          </Title>
        )}
        <Divider/>
        {accumulatedBooks.length === 0 && activeSearch && !isLoading && (
          <Center>
            <Text size="lg" c="dimmed" ta="center">
              No books found for "{activeSearch}"
            </Text>
          </Center>
        )}
        {accumulatedBooks.length > 0 && (
          <Stack>
            {accumulatedBooks.map((book) => (
              <>
                <BookCard key={book.id} {...book} />
                <Divider size="xs"/>
              </>
            ))}
          </Stack>
        )}
        {searchResults?.has_more ? (
          <Button onClick={handleLoadMore}>Load more</Button>
        ) : accumulatedBooks.length > 0 && !isLoading && (
          <Center>
            <Text size="lg" c="dimmed" ta="center">
              No more books found for "{activeSearch}"
            </Text>
          </Center>
        )}
        {isLoading && (
          <Center>
            <Loader size="xl" />
          </Center>
        )}
      </Stack>
    </Center>
  );
} 