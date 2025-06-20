import { Center, Stack, Title, Divider } from "@mantine/core";
import BookCard from "../components/BookCard";
import { useBookSearch } from "../hooks/useBooks";
import { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";

export default function Search() {
  const [searchParams] = useSearchParams();
  const [activeSearch, setActiveSearch] = useState("");
  const { data: searchResults } = useBookSearch(activeSearch);

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