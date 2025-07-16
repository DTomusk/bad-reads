import { Stack, Text, Group, Center } from "@mantine/core";

const generateEmojis = (rating: number | undefined, emoji: string) => {
    const safeRating = rating ?? 0;
    const filledCount = Math.max(0, Math.min(5, Math.round(safeRating)));
    const emptyCount = 5 - filledCount;
    
    return (
        <>
            {Array.from({ length: filledCount }, (_, i) => (
                <Text key={`filled-${i}`} c="white" size="xl">{emoji}</Text>
            ))}
            {Array.from({ length: emptyCount }, (_, i) => (
                <Text key={`empty-${i}`} c="white" size="xl" style={{ opacity: 0.3 }}>{emoji}</Text>
            ))}
        </>
    );
};

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
                {generateEmojis(average_love_rating, '💖')} <Text>{average_love_rating}</Text>
            </Group>
            <Group gap="xs">
                {generateEmojis(average_shit_rating, '💩')} <Text>{average_shit_rating}</Text>
            </Group>
            <Text c="white" size="sm" mb="sm">({number_of_ratings})</Text>
        </Stack>) : (
            <Center>
                <Text c="white" size="sm" mb="sm">No ratings yet</Text>
            </Center>
        )}
        </>
    );
} 