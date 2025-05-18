import {
  Card,
  Image,
  Text,
  Badge,
  Button,
  Group,
  Stack,
  Modal,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { useNavigate } from "react-router-dom";
import RatingGroup from "./RatingGroup";
import { TBook } from "../types/book";

export default function BookCard({
  title,
  author,
  picture = "",
  description,
  uuid,
}: TBook) {
  const navigate = useNavigate();
  const [
    ratingModalOpened,
    { open: openRatingModal, close: closeRatingModal },
  ] = useDisclosure(false);

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
      <Card
        shadow="sm"
        padding="lg"
        radius="md"
        withBorder
        style={{ width: "20rem", height: "20rem" }}
      >
        <Card.Section>
          <Image src={picture} height={160} alt={`${title} image`} />
        </Card.Section>

        <Group justify="space-between" mt="md" mb="xs">
          <Text fw={500}>{title}</Text>
          <Badge color="orange">{author}</Badge>
        </Group>

        <Text size="sm" c="dimmed" lineClamp={6}>
          {description}
        </Text>

        <Group justify="center">
          <Button
            color="blue"
            mt="md"
            radius="md"
            onClick={() => navigate(`book/${uuid}`)}
          >
            More
          </Button>
          <Button color="orange" mt="md" radius="md" onClick={openRatingModal}>
            Rate
          </Button>
        </Group>
      </Card>
    </>
  );
}
