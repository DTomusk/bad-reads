import {
  Group,
  Stack,
  Image,
  Paper,
  Pill,
  Divider,
  ActionIcon,
} from "@mantine/core";
import { TBook } from "../types/book";
import RatingGroup from "../components/RatingGroup";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";
export default function Book() {
  const navigate = useNavigate();
  const testBook: TBook = {
    title: "Book 2",
    description: "lorem ipsum text to continue here",
    picture: "/cats/cat-film.jpeg",
    author: "John Smith",
    uuid: "qwer",
  };
  return (
    <Stack>
      <ActionIcon
        variant="subtle"
        size="xl"
        onClick={() => navigate("/")}
        color="orange"
      >
        <FontAwesomeIcon icon={faArrowLeft} size="3x" />
      </ActionIcon>
      <Group justify="center">
        <Group>
          <Image
            src={testBook.picture}
            height={500}
            alt={`${testBook.title} image`}
          />
          <Paper>
            <h1>{testBook.title}</h1>
            <Divider my="md" />

            <Pill size="xl">{testBook.author}</Pill>
            <Divider my="md" />

            <p>{testBook.description}</p>
            <RatingGroup changeFunction={() => {}} />
          </Paper>
        </Group>
      </Group>
    </Stack>
  );
}
