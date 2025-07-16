import { Stack, Title, Text } from "@mantine/core";
import { ReviewResponse } from "../types/bookDetailResponse";

interface ReviewDisplayProps {
    review: ReviewResponse; 
}

export default function ReviewDisplay({ review }: ReviewDisplayProps) {
    return (
        <Stack>
            <Title order={3}>{review.user_id}</Title>
            <Text>{review.love_score}</Text>
            <Text>{review.shit_score}</Text>
            <Text>{review.text}</Text>
        </Stack>
    )
}