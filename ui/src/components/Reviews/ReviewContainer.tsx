import { Stack, Title, Divider, Group, Loader, Text } from "@mantine/core";
import ReviewDisplay from "./ReviewDisplay";
import Dropdown from "../Shared/Dropdown";
import { ReviewResponse } from "../../types/reviewResponse";
import { useAuth } from "../../auth/AuthProvider";

interface ReviewContainerProps {
    sort: string;
    updateSort: (value: string) => void;
    reviews: ReviewResponse[];
    isLoadingReviews: boolean;
    errorReviews: Error | null;
}

export default function ReviewContainer({ sort, updateSort, reviews, isLoadingReviews, errorReviews }: ReviewContainerProps) {
    const { isAuthenticated } = useAuth();

    return (
        <>
            {isLoadingReviews && <Loader size="xl" />}
            {errorReviews && <Text c="red">Error loading reviews: {(errorReviews as Error)?.message || "Error loading reviews"}</Text>}
            {!isLoadingReviews && !errorReviews && <Stack>
                <Group justify="space-between">
                    <Title order={2}>Reviews</Title>
                    <Dropdown data={["Newest", "Oldest"]} value={sort} onValueChange={updateSort} />
                </Group>
                <Divider />
                {!reviews || reviews.length === 0 && isAuthenticated && <Text mb="xl">No reviews yet, be the first to leave a review!</Text>}
                {!reviews || reviews.length === 0 && !isAuthenticated && <Text mb="xl">No reviews yet, log in and be the first to leave a review!</Text>}
                {reviews && reviews.map((review) => (
                    <ReviewDisplay key={review.id} review={review} />
                ))}
            </Stack>}
        </>
    )
}