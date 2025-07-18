import { Stack, Title, Divider, Group, Loader, Text } from "@mantine/core";
import ReviewDisplay from "./ReviewDisplay";
import Dropdown from "../Shared/Dropdown";
import { useState } from "react";
import { useReviews } from "../../hooks/useReviews";

interface ReviewContainerProps {
    bookId: string;
}

export default function ReviewContainer({ bookId }: ReviewContainerProps) {
    const [sort, setSort] = useState<string>("Newest");
    const { data: reviews, isLoading, error } = useReviews(bookId, sort);
    return (
        <>
            {isLoading && <Loader size="xl" />}
            {error && <Text c="red">Error loading reviews: {(error as Error)?.message || "Error loading reviews"}</Text>}
            {!isLoading && !error && <Stack>
                <Group justify="space-between">
                    <Title order={2}>Reviews</Title>
                    <Dropdown data={["Newest", "Oldest"]} onValueChange={setSort} />
                </Group>
                <Divider />
                {!reviews || reviews.length === 0 && <Text mb="xl">No reviews yet, be the first to leave a review!</Text>}
                {reviews && reviews.map((review) => (
                    <ReviewDisplay key={review.id} review={review} />
                ))}
            </Stack>}
        </>
    )
}