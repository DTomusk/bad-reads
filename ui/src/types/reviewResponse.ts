export type ReviewResponse = {
    id: string;
    book_id: string;
    user_id: string;
    text: string;
    love_score: number;
    shit_score: number;
    date_created: string;
}