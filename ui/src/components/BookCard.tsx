import {
  Text,
  Stack,
  Image,
  Flex,
  Box,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { TBook } from "../types/book";
import RatingModal from "./RatingModal";
import BookActions from "./BookActions";

export default function BookCard({
  title,
  authors,
  picture_url = "",
  id,
}: TBook) {
  const [ratingModalOpened, { open: openRatingModal, close: closeRatingModal }] = useDisclosure(false);

  const handleRatingSubmit = (rating: { hearts: number; poos: number; review: string }) => {
    console.log("Rating submitted:", rating);
    // TODO: Implement rating submission
  };

  return (
    <>
      <RatingModal
        opened={ratingModalOpened}
        onClose={closeRatingModal}
        onSubmit={handleRatingSubmit}
      />
      
      <Flex
        gap="md"
        p="lg"
        h="10rem"
      >
        <Box>
          <Image 
            src={picture_url} 
            height="100%"
            alt={`${title} image`} 
            fit="contain"
          />
        </Box>

        <Stack justify="space-between" h="100%" style={{ flex: 1 }}>
          <Text fw={500} size="lg">{title}</Text>
          <Text>{authors.map((author) => author.name).join(", ")}</Text>

          <BookActions
            bookId={id}
            onRateClick={openRatingModal}
            showMore={true}
          />
        </Stack>
      </Flex>
    </>
  );
}
