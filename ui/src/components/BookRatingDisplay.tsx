import { Stack, Text, Group, Center } from "@mantine/core";

interface BookRatingDisplayProps {
    average_love_rating?: number;
    average_shit_rating?: number;
    number_of_ratings?: number;
}

export default function BookRatingDisplay({
    average_love_rating = 0,
    average_shit_rating = 0,
    number_of_ratings = 0,
}: BookRatingDisplayProps) {
    return (
        <>
        {number_of_ratings > 0 ? (<Stack gap="xs" align="center">
            <Group gap="xs">
                <Text>💖 {average_love_rating}</Text>
            </Group>
            <Group gap="xs">
                <Text>💩 {average_shit_rating}</Text>
            </Group>
            <Text c="white" size="sm" mb="sm">{number_of_ratings > 1 ? `${number_of_ratings} ratings` : `${number_of_ratings} rating`}</Text>
        </Stack>) : (
            <Center>
                <Text c="white" size="sm" mb="sm">No ratings yet</Text>
            </Center>
        )}
        </>
    );
} 