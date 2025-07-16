import { Stack, Title, Text } from "@mantine/core";
import { ReviewResponse } from "../types/reviewResponse";
import EmojiScore from "./Ratings/EmojiScore";

interface ReviewDisplayProps {
    review: ReviewResponse; 
}

export default function ReviewDisplay({ review }: ReviewDisplayProps) {
    return (
        <Stack>
            <Title order={3}>{review.user_id} wrote on {new Date(review.date_created).toLocaleDateString()}</Title>
            <EmojiScore love_score={review.love_score} shit_score={review.shit_score} />
            <Text>{review.text}</Text>
        </Stack>
    )
}