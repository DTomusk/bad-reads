import {
  Card,
  Group,
  Text,
  RingProgress,
  Avatar,
  Image,
  Box,
} from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { TBookClub } from "../types/bookClub";
const stats = [
  { value: 447, label: "Remaining" },
  { value: 76, label: "In progress" },
];
export default function BookClubCard({
  name,
  id,
}: Partial<TBookClub> & { id: string }) {
  const currentDate = new Date().getDate();
  const meetingDate = currentDate + 10;
  const lastMeetingDate = currentDate - 20;
  const navigate = useNavigate();

  return (
    <Card
      p="xl"
      radius="md"
      bg="var(--mantine-color-dark-0)"
      shadow="sm"
      onClick={() => navigate(`/book-club/${id}`)}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "row",
        }}
      >
        <div>
          <h2>{name}</h2>
          <div style={{ display: "flex", flexDirection: "row" }}>
            <Group justify="space-between" mt="md">
              <Avatar.Group spacing="sm">
                <Avatar radius="xl" />
                <Avatar radius="xl" />
                <Avatar radius="xl" />
                <Avatar radius="xl">+5</Avatar>
              </Avatar.Group>
              koi
            </Group>
            <div style={{ marginLeft: "1rem" }}>
              <Text>15</Text>
              <Text c="dimmed">Books Read</Text>
            </div>
            <div style={{ marginLeft: "1rem" }}>
              <Text>4</Text>
              <Text c="dimmed">Average Rating</Text>
            </div>
          </div>
        </div>

        <div style={{ marginLeft: "1rem" }}>
          <RingProgress
            roundCaps
            thickness={6}
            size={150}
            sections={[
              {
                value:
                  ((currentDate - lastMeetingDate) /
                    (meetingDate - lastMeetingDate)) *
                  100,
                color: "green",
              },
            ]}
            label={
              <div>
                <Text ta="center" fz="xs" c="dimmed">
                  Meeting in
                </Text>
                <Text ta="center" fz="lg">
                  {meetingDate - currentDate + " "}
                  Days
                </Text>
              </div>
            }
          />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <Text ta="center" fz="lg">
            Currently Reading
          </Text>
          <Box>
            <Image
              src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-7.png"
              height="100%"
              alt={`test image`}
              fit="contain"
              fallbackSrc="https://placehold.co/600x400?text=Placeholder"
              style={{ width: "15rem" }}
            />
          </Box>
        </div>
      </div>
    </Card>
  );
}
