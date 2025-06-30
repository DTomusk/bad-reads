import { TBook } from "./book";

export type TMeeting = {
    id: string;
    resultsAvailable:boolean;
    book: string;
    date: Date;
    avgPoo?: number;
    avgHeart?: number;
}
