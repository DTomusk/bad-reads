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
  Title,
} from "@mantine/core";
import { useParams } from "react-router-dom";
import { useBook } from "../hooks/useBooks";
import { useDisclosure } from "@mantine/hooks";
import RatingModal from "../components/Ratings/RatingModal";
import BookRatingDisplay from "../components/Ratings/RatingDisplay";
import { useAuth } from "../auth/AuthProvider";
import { ExpandableText } from "../components/Shared/ExpandableText";
import ReviewContainer from "../components/Reviews/ReviewContainer";
import EmojiScoreExpanded from "../components/Ratings/EmojiScoreExpanded";

export default function Book() {
  const { id } = useParams();
  const { data: book, isLoading, error } = useBook(id || "");
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
    <Stack mt="xl">
      <Flex direction="row" gap="md" align="center">
        <Stack>
        <Image
          w="auto" 
          fit="contain" 
          src={book.picture_url}
          alt={`${book.title} image`}
        />
        {isAuthenticated && <Button
              onClick={openRatingModal}
            >
              Rate
            </Button>}
        </Stack>
        <Flex direction="column" gap="md">
            <Title order={1}>{book.title}</Title>
                  {book.authors && book.authors.length > 0 ? (
                    <Title order={3}>{book.authors.join(", ")}</Title>
                  ) : (
                    <Text c="dimmed">No authors listed</Text>
                  )}
            <EmojiScoreExpanded 
                love_score={book.average_love_rating} 
                shit_score={book.average_shit_rating} 
                number_of_ratings={book.number_of_ratings} 
                align="left"
                size="large"
                />
        </Flex>
      </Flex>

      <Stack mb="xl">
        <Title mt="lg" order={2}>Synopsis</Title>
        <Divider />
        <ExpandableText text={book.description}/>
      </Stack>

      <ReviewContainer bookId={id || ""} />

      <RatingModal
        opened={ratingModalOpened}
        onClose={closeRatingModal}
        bookTitle={book.title}
        bookId={id || ""}
      />
    </Stack>
  );
}
