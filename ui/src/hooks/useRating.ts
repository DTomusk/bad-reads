import { useMutation, UseMutationResult } from "@tanstack/react-query";
import { apiClient } from "../api/apiClient";

interface RatingData {
  hearts: number;
  poos: number;
  review: string;
}

interface RatingResponse {
  message: string;
}

export const useRating = (bookId: string): UseMutationResult<RatingResponse, Error, RatingData> => {
  return useMutation({
    mutationFn: async (data: RatingData) => {
      const trimmedReview = data.review.trim();
      
      if (!trimmedReview) {
        const response = await apiClient.post<RatingResponse>(
          `/books/${bookId}/rate`,
          {
            love_score: data.hearts,
            shit_score: data.poos,
          }
        );
        return response.data;
      }

      const response = await apiClient.post<RatingResponse>(
        `/books/${bookId}/review`,
        {
          love_score: data.hearts,
          shit_score: data.poos,
          text: data.review,
        }
      );
      return response.data;
    },
  });
};
