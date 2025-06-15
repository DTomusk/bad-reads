import {
  Group,
  Stack,
  Image,
  Paper,
  Pill,
  Divider,
  ActionIcon,
  Center,
  Loader,
  Text,
  Flex,
} from "@mantine/core";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { useNavigate, useParams } from "react-router-dom";
import { useBook } from "../hooks/useBooks";
import { useDisclosure } from "@mantine/hooks";
import RatingModal from "../components/RatingModal";
import BookActions from "../components/BookActions";
import BookRatingDisplay from "../components/BookRatingDisplay";

export default function Book() {
  const navigate = useNavigate();
  const { id } = useParams();
  const { data: book, isLoading, error } = useBook(id || "");
  const [ratingModalOpened, { open: openRatingModal, close: closeRatingModal }] = useDisclosure(false);

  const handleRatingSubmit = (rating: { hearts: number; poos: number; review: string }) => {
    console.log("Rating submitted:", rating);
    // TODO: Implement rating submission
  };

  if (isLoading) {
    return (
      <Center>
        <Loader size="xl" />
      </Center>
    );
  }

  if (error || !book) {
    return (
      <Center>
        <Text c="red">Error loading book: {(error as Error)?.message || "Book not found"}</Text>
      </Center>
    );
  }

  return (
    <Stack>
      <Group justify="center" mt="xl"> 
        <Flex justify="center" 
          gap={{base: "0", md: "md"}}
          direction={{base: "column", md: "row"}}>
          <Stack>
            <Image
              src={book.picture_url}
              h="auto"
              w="auto"
              fit="contain"
              alt={`${book.title} image`}
              mt="xl"
            />
            <BookRatingDisplay
              average_love_rating={book.average_love_rating}
              average_shit_rating={book.average_shit_rating}
              number_of_ratings={book.number_of_ratings}
            />
            <BookActions
              bookId={id || ""}
              onRateClick={openRatingModal}
            />
          </Stack>
          <Paper style={{ flexGrow: 2 }}>
            <h1>{book.title}</h1>
            <Divider my="md" />

            {book.authors && book.authors.length > 0 ? (
              <Pill size="xl">{book.authors.join(", ")}</Pill>
            ) : (
              <Text c="dimmed">No authors listed</Text>
            )}
            <Divider my="md" />

            <p>{book.description}</p>
          </Paper>
        </Flex>
      </Group>

      <RatingModal
        opened={ratingModalOpened}
        onClose={closeRatingModal}
        onSubmit={handleRatingSubmit}
      />
    </Stack>
  );
}
