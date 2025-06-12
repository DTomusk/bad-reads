import {
  Text,
  Button,
  Group,
  Stack,
  Modal,
  Image,
  Flex,
  Box,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { useNavigate } from "react-router-dom";
import RatingGroup from "./RatingGroup";
import { TBook } from "../types/book";
import { useAuth } from "../auth/AuthProvider";

export default function BookCard({
  title,
  authors,
  picture_url = "",
  id,
}: TBook) {
  const navigate = useNavigate();
  const [
    ratingModalOpened,
    { open: openRatingModal, close: closeRatingModal },
  ] = useDisclosure(false);
  const { isAuthenticated } = useAuth();

  return (
    <>
      <Modal
        opened={ratingModalOpened}
        onClose={closeRatingModal}
        centered
        withCloseButton={false}
      >
        <Stack justify="center">
          <Group justify="center">
            <h2>How bad is the book?</h2>
          </Group>
          <Group justify="center">
            <RatingGroup changeFunction={closeRatingModal} />
          </Group>
        </Stack>
      </Modal>
      
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

          <Group justify="flex-start" mt="auto">
            <Button
              color="blue"
              radius="md"
              onClick={() => navigate(`/book/${id}`)}
            >
              More
            </Button>
            <Button
              color="orange"
              radius="md"
              onClick={openRatingModal}
              disabled={!isAuthenticated}
            >
              Rate
            </Button>
          </Group>
        </Stack>
      </Flex>
    </>
  );
}
