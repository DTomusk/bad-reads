import { useQuery } from "@tanstack/react-query";
import { ReviewResponse } from "../types/reviewResponse";
import { fetcher } from "../api/fetcher";

export const useReviews = (bookId: string, sort: string) => {
    return useQuery<ReviewResponse[]>({
        queryKey: ["reviews", bookId, sort],
        queryFn: async () => {
            const response = await fetcher<ReviewResponse[]>(`/books/${bookId}/reviews?sort=${sort}`);
            return response;
        },
    });
}

