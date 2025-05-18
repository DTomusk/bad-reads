import { Center, Group, Stack } from "@mantine/core";
import BookCard from "../components/BookCard";

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
      </Center>
    </>
  );
}
