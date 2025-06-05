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
} from "@mantine/core";
import RatingGroup from "../components/RatingGroup";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { useNavigate, useParams } from "react-router-dom";
import { useBook } from "../hooks/useBooks";

export default function Book() {
  const navigate = useNavigate();
  const { id } = useParams();
  const { data: book, isLoading, error } = useBook(id || "");

  console.log("Book data:", book);
  console.log("Book ID:", id);

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
          {/*<Image
            src={book.picture}
            height={500}
            alt={`${book.title} image`}
          />*/}
          <Paper>
            <h1>{book.title}</h1>
            <Divider my="md" />

            {book.authors && book.authors.length > 0 ? (
              <Pill size="xl">{book.authors.map((author) => author.name).join(", ")}</Pill>
            ) : (
              <Text c="dimmed">No authors listed</Text>
            )}
            <Divider my="md" />

            {/*<p>{book.description}</p>*/}
            <RatingGroup changeFunction={() => {}} />
          </Paper>
        </Group>
      </Group>
    </Stack>
  );
}
