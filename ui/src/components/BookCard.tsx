import {
  Card,
  Image,
  Text,
  Badge,
  Button,
  Group,
  Stack,
  Modal,
  Grid,
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { useNavigate } from "react-router-dom";
import RatingGroup from "./RatingGroup";
import { TBook } from "../types/book";
import { useAuth } from "../hooks/useAuth";

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
  const isLoggedIn = useAuth();

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
        style={{ width: "100%", maxWidth: "800px", height: "10rem" }}
      >
        <Grid gutter="md" style={{ height: "100%" }}>
          <Grid.Col span="content">
            <Card.Section>
              <Image 
                src={picture_url} 
                height="100%"
                alt={`${title} image`} 
                fit="contain"
              />
            </Card.Section>
          </Grid.Col>

          <Grid.Col span="auto">
            <Stack justify="space-between" h="100%">
              <div>
                <Group justify="space-between" mb="xs">
                  <Text fw={500} size="lg">{title}</Text>
                  <Badge color="orange">{authors.map((author) => author.name).join(", ")}</Badge>
                </Group>
              </div>

              <Group justify="center" mt="auto">
                <Button
                  color="blue"
                  radius="md"
                  onClick={() => navigate(`book/${id}`)}
                >
                  More
                </Button>
                <Button
                  color="orange"
                  radius="md"
                  onClick={openRatingModal}
                  disabled={!isLoggedIn}
                >
                  Rate
                </Button>
              </Group>
            </Stack>
          </Grid.Col>
        </Grid>
      </Card>
    </>
  );
}
