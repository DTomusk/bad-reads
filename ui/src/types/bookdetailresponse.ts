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
}

