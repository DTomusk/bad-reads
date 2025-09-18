import {
  Stack,
  Image,
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
import { useAuth } from "../auth/AuthProvider";
import { ExpandableText } from "../components/Shared/ExpandableText";
import ReviewContainer from "../components/Reviews/ReviewContainer";
import EmojiScoreExpanded from "../components/Ratings/EmojiScoreExpanded";
import { useUserRating } from "../hooks/useRating";
import { useReviews } from "../hooks/useReviews";
import { useState } from "react";

export default function Book() {
  const { id } = useParams();
  const { data: book, isLoading: isLoadingBook, error: errorBook, refetch: refetchBook } = useBook(id || "");
  const [ratingModalOpened, { open: openRatingModal, close: closeRatingModal }] = useDisclosure(false);
  const { isAuthenticated } = useAuth();
  const { data: userRating, isLoading: isLoadingUserRating, refetch: refetchUserRating } = useUserRating(id || "", isAuthenticated);
  const [sort, setSort] = useState<string>("Newest");
  const { data: reviews, isLoading: isLoadingReviews, error: errorReviews, refetch: refetchReviews } = useReviews(id || "", sort);
  const updateSort = (value: string) => {
    setSort(value);
  }

  if (isLoadingBook) {
    return (
      <Center>
        <Loader size="xl" />
      </Center>
    );
  }

  if (errorBook || !book) {
    return (
      <Center>
        <Text c="red">Error loading book: {(errorBook as Error)?.message || "Book not found"}</Text>
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
              disabled={isLoadingUserRating || userRating !== null}
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
                number_of_ratings={book.number_of_ratings || 0} 
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

      <ReviewContainer 
      sort={sort} 
      updateSort={updateSort} 
      reviews={reviews || []} 
      isLoadingReviews={isLoadingReviews} 
      errorReviews={errorReviews as Error | null} 
      />

      <RatingModal
        opened={ratingModalOpened}
        onClose={() => {
          closeRatingModal();
          refetchBook();
          refetchUserRating();
          refetchReviews();
        }}
        bookTitle={book.title}
        bookId={id || ""}
      />
    </Stack>
  );
}
