import { Center, Flex, Group, Stack, Title, useMantineTheme, Divider } from "@mantine/core";
import { useMediaQuery } from '@mantine/hooks';
import BookCardSmall from "./BookCardSmall";
import { TBook } from "../types/book";

export default function BookRow({ books }: { books: TBook[] }) {
    const theme = useMantineTheme();
    const isXl = useMediaQuery(`(min-width: ${theme.breakpoints.xl})`);
    const isLg = useMediaQuery(`(min-width: ${theme.breakpoints.lg})`);
    const isMd = useMediaQuery(`(min-width: ${theme.breakpoints.md})`);
    
    const CARD_WIDTH = 200; // pixels
    
    // Calculate number of visible items based on screen width
    const getVisibleItems = () => {
        if (isXl) return 6;
        if (isLg) return 5;
        if (isMd) return 4;
        return 3;
    };
    
    return (
        <Stack>
            <Title order={2}>Worst Books of the Month</Title>
            <Divider/>
            <Center>
                <Flex gap="md" wrap="nowrap" style={{ overflow: 'hidden', maxWidth: '100%' }}>
                    {books?.slice(0, getVisibleItems()).map((book) => (
                        <div key={book.id} style={{ width: CARD_WIDTH, flexShrink: 0 }}>
                            <BookCardSmall title={book.title} picture_url={book.picture_url || ""} id={book.id} />
                        </div>
                    ))}
                </Flex>
            </Center>
        </Stack>
    )
}