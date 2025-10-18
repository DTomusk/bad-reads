import { Stack, Title, Divider } from "@mantine/core";
import BookCardSmall from "./BookCardSmall";
import { TBook } from "../../types/book";
import { Carousel } from '@mantine/carousel';

interface BookRowProps {
    row_title: string;
    books: TBook[]
}

export default function BookRow({ row_title, books } : BookRowProps) {
    const CARD_WIDTH = 150; // pixels

    return (
        <Stack>
            <Title order={2}>{row_title}</Title>
            <Divider/>
            <Carousel withIndicators slideSize="25%" slideGap="md" emblaOptions={{loop: false, slidesToScroll: 2}}>
            {books?.map((book) => (
                <Carousel.Slide key={book.id} style={{ width: CARD_WIDTH }}>
                    <BookCardSmall title={book.title} picture_url={book.picture_url || ""} id={book.id} average_love_rating={book.average_love_rating} average_shit_rating={book.average_shit_rating} number_of_ratings={book.number_of_ratings} />
                </Carousel.Slide>))}
            </Carousel>
        </Stack>
    )
}