import { Center, Flex, Stack, Title, Divider } from "@mantine/core";
import BookCardSmall from "./BookCardSmall";
import { TBook } from "../types/book";

export default function BookRow({ books }: { books: TBook[] }) {
    
    const CARD_WIDTH = 150; // pixels
    
    return (
        <Stack>
            <Title order={2}>Worst Books of the Month</Title>
            <Divider/>
            <Center style={{ overflow: 'scroll' }}>
                <Flex gap="md" wrap="nowrap">
                    {books?.map((book) => (
                        <div key={book.id} style={{ width: CARD_WIDTH, flexShrink: 0 }}>
                            <BookCardSmall title={book.title} picture_url={book.picture_url || ""} id={book.id} />
                        </div>
                    ))}
                </Flex>
            </Center>
        </Stack>
    )
}