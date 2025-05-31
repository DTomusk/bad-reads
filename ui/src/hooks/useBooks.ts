import { useQuery } from "@tanstack/react-query";
import { fetcher } from "../api/fetcher";
import { TBook } from "../types/book";

export const useBooks = () => {
    return useQuery({
        queryKey: ["books"],
        queryFn: () => fetcher<TBook[]>("/books"),
    });
}