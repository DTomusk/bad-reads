import { Stack, Title, Text, Divider, Group } from "@mantine/core";
import { ReviewResponse } from "../../types/reviewResponse";
import EmojiScoreExpanded from "../Ratings/EmojiScoreExpanded";

interface ReviewDisplayProps {
    review: ReviewResponse; 
}

export default function ReviewDisplay({ review }: ReviewDisplayProps) {
    return (
        <Stack>
            <Title order={3}>{review.user_id} wrote:</Title>
            <Group gap="md">
                <EmojiScoreExpanded love_score={review.love_score} shit_score={review.shit_score} />
                <Text>{review.text}</Text>
            </Group>
            <Divider my="xs" />
        </Stack>
    )
}