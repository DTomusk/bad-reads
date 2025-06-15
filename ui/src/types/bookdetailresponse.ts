export type BookDetailResponse = {
    id: string;
    title: string;
    authors: string[];
    average_love_rating: number;
    average_shit_rating: number;
    number_of_ratings: number;
    sum_of_love_ratings: number;
    sum_of_shit_ratings: number;
    picture_url?: string;
    description: string;
    reviews: ReviewResponse[];
}

export type ReviewResponse = {
    id: string;
    book_id: string;
    user_id: string;
    text: string;
    love_score: number;
    shit_score: number;
}