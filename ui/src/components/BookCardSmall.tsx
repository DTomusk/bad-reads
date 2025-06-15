import { Stack, Image, Card, Title } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { TBook } from "../types/book";
import BookRatingDisplay from "./BookRatingDisplay";

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

                <BookRatingDisplay 
                    average_love_rating={average_love_rating}
                    average_shit_rating={average_shit_rating}
                    number_of_ratings={number_of_ratings}
                />
            </Stack>
        </Card> 
    )
}