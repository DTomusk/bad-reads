import { Stack, Text } from "@mantine/core";
import EmojiScore from "./EmojiScore";

interface BookRatingDisplayProps {
    average_love_rating?: number;
    average_shit_rating?: number;
    number_of_ratings?: number;
    align?: "center" | "left";
}

export default function BookRatingDisplay({
    average_love_rating = 0,
    average_shit_rating = 0,
    number_of_ratings = 0,
    align = "center",
}: BookRatingDisplayProps) {
    return (
        <>
        {number_of_ratings > 0 ? (
        <Stack gap="xs" align={align}>
            <EmojiScore love_score={average_love_rating} shit_score={average_shit_rating} />
            <Text c="white" size="sm" mb="sm">{number_of_ratings > 1 ? `${number_of_ratings} ratings` : `${number_of_ratings} rating`}</Text>
        </Stack>) : (
            <Text c="white" size="sm" mb="sm" ta={align}>No ratings yet</Text>
        )}
        </>
    );
} 