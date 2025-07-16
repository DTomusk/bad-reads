import { Stack, Title, Divider } from "@mantine/core";
import { ReviewResponse } from "../types/reviewResponse";
import ReviewDisplay from "./ReviewDisplay";

interface ReviewContainerProps {
    reviews: ReviewResponse[];
}

export default function ReviewContainer({ reviews }: ReviewContainerProps) {
    return (
        <Stack>
            <Title order={2}>Top Reviews</Title>
            <Divider my="md" />
            {reviews.map((review) => (
                <ReviewDisplay key={review.id} review={review} />
            ))}
        </Stack>
    )
}