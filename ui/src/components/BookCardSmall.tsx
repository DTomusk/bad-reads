import { Stack, Image, Card, Title, Text } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { TBook } from "../types/book";

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

export default function BookCardSmall({
    title,
    picture_url,
    id,
    average_love_rating = 0,
    average_shit_rating = 0,
    number_of_ratings = 0,
}: Partial<TBook> & { id: string }) {
    const navigate = useNavigate();
    
    return (
        <Card 
            shadow="sm" 
            radius="md" 
            withBorder 
            h="100%" 
            onClick={() => navigate(`/book/${id}`)}
            style={{ cursor: 'pointer' }}
            bg="dark.0"
            styles={{
                root: {
                    transition: 'background-color 0.2s ease',
                    '&:hover': {
                        backgroundColor: 'var(--mantine-color-dark-9)',
                    }
                }
            }}
            p="0"
            m="0"
        >
            <Stack h="100%" justify="space-between" gap="xs">
                {picture_url ? <Image 
                    src={picture_url} 
                    alt={title} 
                    width="100%" 
                    fit="contain" 
                    c="white"
                /> : <Title 
                    order={5} 
                    size="sm" 
                    c="white"
                    m="sm"
                >
                    {title}
                </Title>}

                <Stack gap="xs" align="center">
                    <div style={{ display: 'flex', gap: '2px' }}>
                        {generateEmojis(average_love_rating, '💖')}
                    </div>
                    <div style={{ display: 'flex', gap: '2px' }}>
                        {generateEmojis(average_shit_rating, '💩')}
                    </div>
                    <Text c="white" size="sm" mb="sm">({number_of_ratings})</Text>
                </Stack>
            </Stack>
        </Card> 
    )
}