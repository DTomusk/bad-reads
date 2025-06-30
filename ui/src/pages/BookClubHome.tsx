import { Stack, Title } from "@mantine/core";
import BookClubCard from "../components/BookClubCard";
import { TBookClub } from "../types/bookClub";

export default function BookClubHome() {
  const testBookClub: TBookClub = {
    id: "1234",
    name: "Gritty Book Club",
    book: "test book",
  };
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
      <BookClubCard {...testBookClub} />
    </Stack>
  );
}
