import {
  Group,
  Stack,
  Image,
  Paper,
  Pill,
  Divider,
  Center,
  Loader,
  Text,
  Flex,
  Button,
} from "@mantine/core";
import { useParams } from "react-router-dom";
import { useBook } from "../hooks/useBooks";
import { useDisclosure } from "@mantine/hooks";
import RatingModal from "../components/Ratings/RatingModal";
import BookRatingDisplay from "../components/Ratings/RatingDisplay";
import { useAuth } from "../auth/AuthProvider";
import { ExpandableText } from "../components/Shared/ExpandableText";
import ReviewContainer from "../components/Reviews/ReviewContainer";
import { useReviews } from "../hooks/useReviews";

export default function Book() {
  const { id } = useParams();
  const { data: book, isLoading, error } = useBook(id || "");
  const { data: reviews, isLoading: reviewsLoading, error: reviewsError } = useReviews(id || "");
  const [ratingModalOpened, { open: openRatingModal, close: closeRatingModal }] = useDisclosure(false);
  const { isAuthenticated } = useAuth();

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
            {isAuthenticated && <Button
              onClick={openRatingModal}
            >
              Rate
            </Button>}
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
            <Group mb="xl">
              <ExpandableText text={book.description}/>
            </Group>
            {reviewsLoading && <Loader size="xl" />}
            {reviewsError && <Text c="red">Error loading reviews: {(reviewsError as Error)?.message || "Error loading reviews"}</Text>}
            {reviews && reviews.length > 0 && <ReviewContainer reviews={reviews} />}
          </Paper>
        </Flex>
      </Group>

      <RatingModal
        opened={ratingModalOpened}
        onClose={closeRatingModal}
        bookTitle={book.title}
        bookId={id || ""}
      />
    </Stack>
  );
}
