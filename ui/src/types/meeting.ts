import { TBook } from "./book";

export type TMeeting = {
    id: string;
    resultsAvailable:boolean;
    book: string;
    date: Date;
    avgPoo?: number;
    avgHeart?: number;
}

export type TMeetingReponse =   {
    id: string,
    book_name: string,
    book_club_id: string,
    date: string
  }