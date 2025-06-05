import { TAuthor } from "./author";

export type TBook = {
    id: string;
    title: string;
    authors: TAuthor[];
    //picture?: string;
    //description: string;
    average_rating: number;
    number_of_ratings: number;
    sum_of_ratings: number;
}