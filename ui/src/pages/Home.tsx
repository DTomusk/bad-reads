import { Autocomplete, Center, Group, Stack, Title } from "@mantine/core";
import BookCard from "../components/BookCard";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
const test = [
  {
    title: "Book 1",
    description: "lorem ipsum text to continue here",
    author: "Jane Doe",
    picture: "/cats/cat-film.jpeg",
    uuid: "asdf",
  },
  {
    title: "Book 2",
    description: "lorem ipsum text to continue here",
    picture: "/cats/cat-food.jpeg",
    author: "John Smith",
    uuid: "qwer",
  },
  {
    title: "Book 3",
    description: "lorem ipsum text to continue here",
    picture: "/cats/cat-shop.jpg",
    author: "Emily Blunt",
    uuid: "zxcv",
  },
  {
    title: "Book 4",
    description: "lorem ipsum text to continue here",
    picture: "/cats/cat-sport.jpg",
    author: "Taylor Swift",
    uuid: "tyui",
  },
];

export default function Home() {
  return (
    <>
      <Center>
        <Stack>
          <Title
            style={{
              color: "var(--mantine-color-orange-filled)",
              alignSelf: "center",
            }}
          >
            Welcome to Bad Reads
          </Title>
          <Autocomplete
            placeholder="Search for bad books"
            leftSection={<FontAwesomeIcon icon={faMagnifyingGlass} />}
            data={[]}
            size="xl"
            visibleFrom="xs"
            style={{ alignSelf: "center", width: "50rem" }}
          />
          <Group justify="center">
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
            {test.map((item) => (
              <BookCard {...item} />
            ))}
          </Group>
        </Stack>
      </Center>
    </>
  );
}
