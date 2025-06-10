import { useQuery } from "@tanstack/react-query";
import { fetcher } from "../api/fetcher";
import { TBook } from "../types/book";

export const useBooks = () => {
    return useQuery({
        queryKey: ["books"],
        queryFn: () => fetcher<TBook[]>("/books"),
    });
}

export const useBook = (id: string) => {
    return useQuery({
        queryKey: ["book", id],
        queryFn: async () => {
            const response = await fetcher<{ book: TBook, ratings: any[] }>(`/books/${id}`);
            return response.book;
        },
    });
}

export const useBookSearch = (query: string) => {
    return useQuery({
        queryKey: ["books", query],
        queryFn: () => fetcher<TBook[]>(`/books/search?query=${query}`),
    });
}
