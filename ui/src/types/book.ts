import { TAuthor } from "./author";

export type TBook = {
    title: string;
    authors: TAuthor[];
    average_rating: number;
    number_of_ratings: number;
    sum_of_ratings: number;
    picture_url?: string;
    description: string;
    id: string;
}