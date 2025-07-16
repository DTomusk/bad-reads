import { useQuery } from "@tanstack/react-query";
import { fetcher } from "../api/fetcher";
import { TBook } from "../types/book";
import { BookDetailResponse } from "../types/bookdetailresponse";
import { BookSearchResponse } from "../types/bookSearchResponse";

export const useBooks = () => {
    return useQuery({
        queryKey: ["books"],
        queryFn: () => fetcher<TBook[]>("/books/"),
    });
}

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
