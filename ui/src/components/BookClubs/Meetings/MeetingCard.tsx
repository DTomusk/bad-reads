import { faHeart, faList, faPoo } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  Accordion,
  AccordionItem,
  Card,
  Text,
  Notification,
} from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { TBookClub } from "../types/bookClub";
import { TMeeting, TMeetingReponse } from "../types/meeting";

export default function MeetingCard({
  book_name,
  date,
  // avgPoo,
  // avgHeart,
  // resultsAvailable,
  id,
}: TMeetingReponse) {
  const currentDate = new Date().getDate();
  const meetingDate = currentDate + 10;

  return (
    <Card
      p="xl"
      mt="md"
      radius="md"
      bg="var(--mantine-color-light-0)"
      shadow="sm"
      c="var(--mantine-color-dark-0)"
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Text c="dimmed">Meeting</Text>

        <div
          style={{ display: "flex", flexDirection: "row", flexWrap: "wrap" }}
        >
          <h2>{new Date(date).toLocaleDateString("en-GB")}</h2>
          <h2>- {book_name}</h2>
          {false && (
            <div
              style={{
                display: "flex",
                flexDirection: "row",
                marginLeft: "auto",
              }}
            >
              <div
                style={{
                  marginLeft: "1rem",
                  display: "flex",
                  flexDirection: "row",
                }}
              >
                <Text c="var(--mantine-color-dark-0)" size="3rem">
                  {avgPoo}
                </Text>
                <br />
                <FontAwesomeIcon
                  icon={faPoo}
                  color="Brown"
                  size="3x"
                  style={{ marginLeft: "1rem" }}
                />
              </div>
              <div
                style={{
                  marginLeft: "1rem",
                  display: "flex",
                  flexDirection: "row",
                }}
              >
                <Text c="var(--mantine-color-dark-0)" size="3rem">
                  {/* {avgHeart} */}
                </Text>
                <br />
                <FontAwesomeIcon
                  icon={faHeart}
                  color="red"
                  size="3x"
                  style={{ marginLeft: "1rem" }}
                />
              </div>
            </div>
          )}
        </div>

        {false ? (
          <div style={{ marginLeft: "1rem" }}>
            <Accordion transitionDuration={1000}>
              <AccordionItem value="1">
                <Accordion.Control>Voting Details</Accordion.Control>
                <Accordion.Panel>
                  Colors, fonts, shadows and many other parts are customizable
                  to fit your design needs
                </Accordion.Panel>
              </AccordionItem>
            </Accordion>
          </div>
        ) : new Date(date) < new Date() ? (
          <Notification
            withCloseButton={false}
            color="green"
            radius="md"
            title="Meeting Has Not Happened Yet"
          ></Notification>
        ) : (
          <Notification
            withCloseButton={false}
            color="red"
            radius="md"
            title="Meeting Results Not Available Yet"
          ></Notification>
        )}
      </div>
    </Card>
  );
}
