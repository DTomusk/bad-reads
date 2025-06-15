import {
  Modal,
  Stack,
  Group,
  Text,
  Button,
  Textarea,
  Title,
} from "@mantine/core";
import { useState } from "react";
import RatingGroup from "./RatingGroup";

interface RatingModalProps {
  opened: boolean;
  onClose: () => void;
  onSubmit: (rating: { hearts: number; poos: number; review: string }) => void;
}

export default function RatingModal({ opened, onClose, onSubmit }: RatingModalProps) {
  const [hearts, setHearts] = useState(0);
  const [poos, setPoos] = useState(0);
  const [review, setReview] = useState("");

  const handleSubmit = () => {
    onSubmit({ hearts, poos, review });
    onClose();
  };

  return (
    <Modal
      opened={opened}
      onClose={onClose}
      centered
      withCloseButton={false}
      size="lg"
    >
      <Stack gap="xl">
        <Title order={2} ta="center">How bad is the book?</Title>
        
        <Stack gap="md">
          <Text fw={500}>Hearts Rating:</Text>
          <RatingGroup 
            changeFunction={(value: number) => setHearts(value)} 
            icon="heart"
          />
        </Stack>

        <Stack gap="md">
          <Text fw={500}>Poos Rating:</Text>
          <RatingGroup 
            changeFunction={(value: number) => setPoos(value)} 
            icon="poo"
          />
        </Stack>

        <Textarea
          label="Review (optional)"
          placeholder="Share your thoughts about the book..."
          value={review}
          onChange={(event) => setReview(event.currentTarget.value)}
          minRows={3}
        />

        <Group justify="flex-end" mt="md">
          <Button variant="subtle" onClick={onClose}>
            Cancel
          </Button>
          <Button onClick={handleSubmit}>
            Submit
          </Button>
        </Group>
      </Stack>
    </Modal>
  );
} 