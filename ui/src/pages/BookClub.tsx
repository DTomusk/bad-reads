import {
  Card,
  Group,
  Avatar,
  RingProgress,
  Button,
  Paper,
  Stack,
  Modal,
  Center,
  Text,
  Loader,
} from "@mantine/core";
import MeetingCard from "../components/MeetingCard";
import { TMeeting } from "../types/meeting";
import { useDisclosure } from "@mantine/hooks";
import { AddMeetingForm } from "../components/AddMeetingForm";
import { AddMemberForm } from "../components/AddMemberForm";
import { useParams } from "react-router-dom";
import { useBookClub } from "../hooks/useBookClubs";

export default function BookClub() {
  let params = useParams();
  const { data: bookclub, isLoading, error } = useBookClub(params.id || "");

  const [
    newMeetingModalOpened,
    { open: openMeetingModal, close: closeMeetingModal },
  ] = useDisclosure(false);
  const [
    newMemberModalOpened,
    { open: openMemberModal, close: closeMemberModal },
  ] = useDisclosure(false);
  const meetingCardExample: TMeeting = {
    id: "123",
    book: "A Psalm of the wild built",
    date: new Date(),
    resultsAvailable: true,
    avgHeart: 3,
    avgPoo: 2,
  };

  if (isLoading) {
    return (
      <Center>
        <Loader size="xl" />
      </Center>
    );
  }

  if (error || !bookclub) {
    return (
      <Center>
        <Text c="red">
          Error loading book club:{" "}
          {(error as Error)?.message || "Book club not found"}
        </Text>
      </Center>
    );
  }

  return (
    <>
      <Modal
        opened={newMeetingModalOpened}
        onClose={closeMeetingModal}
        title="Add New Meeting"
        styles={{
          body: {
            backgroundColor: "#fff",
            color: "black",
          },
        }}
      >
        <AddMeetingForm />
      </Modal>
      <Modal
        opened={newMemberModalOpened}
        onClose={closeMemberModal}
        title="Add New User"
        styles={{
          body: {
            backgroundColor: "#fff",
            color: "black",
          },
        }}
      >
        <AddMemberForm />
      </Modal>
      <Card p="xl" radius="md" bg="var(--mantine-color-dark-0)" shadow="sm">
        <div
          style={{
            display: "flex",
            flexDirection: "row",
          }}
        >
          <div
            style={{
              display: "flex",
              flexDirection: "row",
            }}
          >
            <div>
              <h1>{bookclub?.name}</h1>
              <div style={{ display: "flex", flexDirection: "row" }}>
                <Group justify="space-between" mt="md">
                  <Avatar.Group spacing="sm">
                    <Avatar radius="xl" />
                    <Avatar radius="xl" />
                    <Avatar radius="xl" />
                    <Avatar radius="xl">+5</Avatar>
                  </Avatar.Group>
                  Members
                </Group>
              </div>
            </div>
          </div>
          <Card
            bg="var(--mantine-color-light-0)"
            radius="md"
            padding="md"
            ml="auto"
          >
            <Stack>
              <Button
                color="var(--mantine-color-teal)"
                radius="md"
                onClick={openMemberModal}
              >
                Add New Member
              </Button>
              <Button
                color="var(--mantine-color-teal)"
                radius="md"
                onClick={openMeetingModal}
              >
                Add New Meeting
              </Button>
            </Stack>
          </Card>
        </div>
      </Card>
      {bookclub ? (
        bookclub.meetings?.map((meeting) => <MeetingCard {...meeting} />)
      ) : (
        <Text>No Meetings Found</Text>
      )}
    </>
  );
}
