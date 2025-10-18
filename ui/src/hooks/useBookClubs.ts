import { useQuery } from "@tanstack/react-query";
import { fetcher } from "../api/fetcher";
import { TBookClubResponse } from "../types/bookClub";

export const useBookClubs = () => {
    return useQuery({
        queryKey: ["book_clubs"],
        queryFn: () => fetcher<TBookClubResponse[]>("/book-clubs"),
    });
}

export const useBookClub = (id: string) => {
    return useQuery({
        queryKey: ["book_club", id],
        queryFn: async () => {
            const response = await fetcher<TBookClubResponse>(`/book-clubs/${id}`);
            return response;
        },
    });
}
