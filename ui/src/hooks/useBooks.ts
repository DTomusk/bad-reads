import { useQuery } from "@tanstack/react-query";
import { fetcher } from "../api/fetcher";
import { TBook } from "../types/book";
import { BookDetailResponse } from "../types/bookdetailresponse";
import { BookSearchResponse } from "../types/bookSearchResponse";
import { BookWithReviewResponse } from "../types/bookwithreviewresponse";

type UseBooksParams = {
  page?: number;
  page_size?: number;
  sort_by?: "alphabetical" | "most_loved" | "most_poos";
  sort_order?: "asc" | "desc";
};

export const useBooks = ({
  page = 1,
  page_size = 10,
  sort_by = "most_loved",
  sort_order = "desc",
}: UseBooksParams = {}) => {
  return useQuery({
    queryKey: ["books", { page, page_size, sort_by, sort_order }],
    queryFn: () =>
      fetcher<TBook[]>(
        `/books/?page=${page}&page_size=${page_size}&sort_by=${sort_by}&sort_order=${sort_order}`
      ),
  });
};

export const useBook = (id: string) => {
    return useQuery({
        queryKey: ["book", id],
        queryFn: async () => {
            const response = await fetcher<BookDetailResponse>(`/books/${id}`);
            return response;
        },
    });
}

export const useBookSearch = (query: string, page: number) => {
    return useQuery({
        queryKey: ["books", query, page],
        queryFn: () => fetcher<BookSearchResponse>(`/books/search?query=${query}&page=${page}`),
    });
}

export const useMyBookReviews = () => {
    return useQuery<BookWithReviewResponse[]>({
        queryKey: ['my-book-reviews'],
        queryFn: async () => {
            const response = await fetcher<BookWithReviewResponse[]>('/books/my-reviews');
            return response;
        }
    })
}
