import { useQuery } from "@tanstack/react-query";
import { ReviewResponse } from "../types/reviewResponse";
import { fetcher } from "../api/fetcher";

export const useReviews = (bookId: string) => {
    return useQuery<ReviewResponse[]>({
        queryKey: ["reviews", bookId],
        queryFn: async () => {
            const response = await fetcher<ReviewResponse[]>(`/books/${bookId}/reviews`);
            return response;
        },
    });
}

