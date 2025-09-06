import { TBook } from "./book";
import { ReviewResponse } from "./reviewResponse";

export type BookWithReviewResponse = {
    review: ReviewResponse;
    book: TBook
}