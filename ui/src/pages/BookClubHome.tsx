import { Center, Loader, Stack, Title, Text } from "@mantine/core";
import BookClubCard from "../components/BookClubCard";
import { useBookClubs } from "../hooks/useBookClubs";

export default function BookClubHome() {
  const { data: bookclubs, isLoading, error } = useBookClubs();

  // const testBookClub: TBookClub = {
  //   id: "1234",
  //   name: "Gritty Book Club",
  //   book: "test book",
  // };

  if (isLoading) {
    return (
      <Center>
        <Loader size="xl" />
      </Center>
    );
  }

  if (error || !bookclubs) {
    return (
      <Center>
        <Text c="red">
          Error loading book clubs:{" "}
          {(error as Error)?.message || "Book clubs not found"}
        </Text>
      </Center>
    );
  } else {
    return (
      <Stack>
        <br />
        <Title
          order={1}
          style={{
            alignSelf: "center",
            fontSize: "54px",
          }}
          c="white"
        >
          💅 Book Clubs 🫡
        </Title>
        <br />
        {bookclubs?.map((item) => (
          <BookClubCard {...item} />
        ))}
      </Stack>
    );
  }
}
