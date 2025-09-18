import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { ReviewResponse } from "../types/reviewResponse";
import { fetcher } from "../api/fetcher";
import { apiClient } from "../api/apiClient";

export const useReviews = (bookId: string, sort: string) => {
    return useQuery<ReviewResponse[]>({
        queryKey: ["reviews", bookId, sort],
        queryFn: async () => {
            const response = await fetcher<ReviewResponse[]>(`/books/${bookId}/reviews?sort=${sort.toLowerCase()}`);
            return response;
        },
    });
}

export const useUserReview = (
  bookId: string,
  isAuthenticated: boolean
): UseQueryResult<ReviewResponse | null, Error> => {
  return useQuery({
    queryKey: ["userRating", bookId],
    queryFn: async () => {
      const response = await apiClient.get<ReviewResponse>(
        `/books/${bookId}/review`
      );
      console.log(response.data)
      return response.data;
    },
    enabled: isAuthenticated && !!bookId,
    retry: false,
  });
};
