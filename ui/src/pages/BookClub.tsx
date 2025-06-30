import {
  Card,
  Group,
  Avatar,
  RingProgress,
  Text,
  Button,
  Paper,
  Stack,
  Modal,
} from "@mantine/core";
import MeetingCard from "../components/MeetingCard";
import { TMeeting } from "../types/meeting";
import { useState } from "react";
import { useDisclosure } from "@mantine/hooks";
import { AddMeetingForm } from "../components/AddMeetingForm";
import { AddMemberForm } from "../components/AddMemberForm";

export default function BookClub() {
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
              <h1>Gritty Book Club</h1>
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

      <MeetingCard {...meetingCardExample} />
    </>
  );
}
