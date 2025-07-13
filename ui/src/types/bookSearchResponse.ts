import { TBook } from "./book";

export type BookSearchResponse = {
    books: TBook[];
    has_more: boolean;
}