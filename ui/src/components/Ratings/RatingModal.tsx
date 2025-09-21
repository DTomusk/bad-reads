import {
  Modal,
  Stack,
  Group,
  Button,
  Title,
  Card,
} from "@mantine/core";
import { useState } from "react";
import { useQueryClient } from "@tanstack/react-query";
import RatingGroup from "./RatingGroup";
import LimitedTextarea from "../Shared/LimitedTextarea";
import { useRating } from "../../hooks/useRating";

interface RatingModalProps {
  opened: boolean;
  onClose: () => void;
  bookTitle: string;
  bookId: string;
  love_score: number
  shit_score: number
  text: string
  rating_id: string;
  review_id: string;
}

const getBadRatingText = (value: number) => {
  if (value === 0) return "Flawless";
  if (value <= 1) return "Doesn't do much wrong";
  if (value <= 2) return "Bad at times";
  if (value <= 3) return "Quite bad";
  if (value <= 4) return "Awful";
  return "An absolute trainwreck";
};

const getGoodRatingText = (value: number) => {
  if (value === 0) return "There is nothing positive about this book";
  if (value <= 1) return "It's alright";
  if (value <= 2) return "It has its moments";
  if (value <= 3) return "I quite enjoyed it";
  if (value <= 4) return "I loved it";
  return "It was completely life changing";
};

export default function RatingModal({ opened, onClose, bookTitle, bookId, love_score, shit_score, text }: RatingModalProps) {
  const [hearts, setHearts] = useState(love_score);
  const [poos, setPoos] = useState(shit_score);
  const [review, setReview] = useState(text);
  const queryClient = useQueryClient();
  const { mutate: submitRating, isPending: isLoading } = useRating(bookId);

  const handleSubmit = () => {
    submitRating(
      { hearts, poos, review },
      {
        onSuccess: () => {
          // Invalidate the book query to refresh the data
          queryClient.invalidateQueries({ queryKey: ["book", bookId] });
          onClose();
        },
        onError: () => {
          // Keep modal open on error so user can try again
          // TODO: show error message
        }
      }
    );
  };

  return (
    <Modal
      opened={opened}
      onClose={onClose}
      centered
      withCloseButton={false}
      size="lg"
    >
      <Card>
        <Card.Section bg="teal.0">
          <Title order={2} ta="center" p="md">Rate {bookTitle}</Title>
        </Card.Section>

        <Card.Section bg="light" c="dark.9">
          <Stack gap="xl" p="md" align="center">
            <Stack gap="md" align="center">
              <Title order={3} c="dark.9">How bad is the book?</Title>
              <RatingGroup 
                changeFunction={(value: number) => setPoos(value)} 
                icon="poo"
                value={poos}
                getRatingText={getBadRatingText}
                filledColor="#8B4513"
              />
            </Stack>
            <Stack gap="md" align="center">
              <Title order={3} c="dark.9">How much did you love it?</Title>
              <RatingGroup 
                changeFunction={(value: number) => setHearts(value)} 
                icon="heart"
                value={hearts}
                getRatingText={getGoodRatingText}
              />
            </Stack>

            <LimitedTextarea
              title="Review (optional)"
              maxLength={500}
              placeholder="Share your thoughts about the book..."
              value={review}
              onChange={setReview}
            />
          </Stack>
        </Card.Section>

        <Card.Section bg="teal.0">
          <Group justify="flex-end" w="100%" p="md">
            <Button bg="secondary.0" onClick={onClose}>
              Cancel
            </Button>
            <Button onClick={handleSubmit} loading={isLoading}>
              Submit
            </Button>
          </Group>
        </Card.Section>
      </Card>
    </Modal>
  );
} 