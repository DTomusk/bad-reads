export type ReviewResponse = {
    review_id?: string;
    rating_id: string;
    book_id: string;
    username: string;
    text?: string;
    love_score: number;
    shit_score: number;
    date_created?: string;
}