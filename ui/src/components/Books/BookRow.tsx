import { Center, Flex, Stack, Title, Divider, ActionIcon } from "@mantine/core";
import { useRef, useState, useEffect } from "react";
import BookCardSmall from "./BookCardSmall";
import { TBook } from "../../types/book";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronLeft, faChevronRight } from "@fortawesome/free-solid-svg-icons";

export default function BookRow({ books }: { books: TBook[] }) {
    const CARD_WIDTH = 150; // pixels
    const scrollRef = useRef<HTMLDivElement>(null);
    const [showLeftArrow, setShowLeftArrow] = useState(false);
    const [showRightArrow, setShowRightArrow] = useState(false);

    const checkScroll = () => {
        if (scrollRef.current) {
            const { scrollLeft, scrollWidth, clientWidth } = scrollRef.current;
            setShowLeftArrow(scrollLeft > 0);
            setShowRightArrow(scrollLeft < scrollWidth - clientWidth - 1);
        }
    };

    useEffect(() => {
        const scrollElement = scrollRef.current;
        if (scrollElement) {
            checkScroll();
            scrollElement.addEventListener('scroll', checkScroll);
            window.addEventListener('resize', checkScroll);
            return () => {
                scrollElement.removeEventListener('scroll', checkScroll);
                window.removeEventListener('resize', checkScroll);
            };
        }
    }, []);

    const scroll = (direction: 'left' | 'right') => {
        if (scrollRef.current) {
            const scrollAmount = CARD_WIDTH * 2; // Scroll by 2 cards at a time
            scrollRef.current.scrollBy({
                left: direction === 'left' ? -scrollAmount : scrollAmount,
                behavior: 'smooth'
            });
        }
    };

    return (
        <Stack>
            <Title order={2}>Worst Books of the Month</Title>
            <Divider/>
            <div style={{ position: 'relative' }}>
                {showLeftArrow && (
                    <ActionIcon
                        variant="filled"
                        color="dark"
                        size="xl"
                        radius="xl"
                        style={{
                            position: 'absolute',
                            left: 0,
                            top: '50%',
                            transform: 'translateY(-50%)',
                            zIndex: 1
                        }}
                        onClick={() => scroll('left')}
                    >
                        <FontAwesomeIcon icon={faChevronLeft} />
                    </ActionIcon>
                )}
                <Center 
                    ref={scrollRef}
                    style={{ 
                        overflow: 'scroll', 
                        display: 'block',
                        position: 'relative',
                        '&::before, &::after': {
                            content: '""',
                            position: 'absolute',
                            top: 0,
                            width: '100px',
                            height: '100%',
                            pointerEvents: 'none',
                            zIndex: 1
                        },
                        '&::before': {
                            left: 0,
                            background: 'linear-gradient(to right, var(--mantine-color-dark-7), transparent)'
                        },
                        '&::after': {
                            right: 0,
                            background: 'linear-gradient(to left, var(--mantine-color-dark-7), transparent)'
                        }
                    }}
                >
                    <Flex gap="md" wrap="nowrap">
                        {books?.map((book) => (
                            <div key={book.id} style={{ width: CARD_WIDTH, flexShrink: 0 }}>
                                <BookCardSmall title={book.title} picture_url={book.picture_url || ""} id={book.id} average_love_rating={book.average_love_rating} average_shit_rating={book.average_shit_rating} number_of_ratings={book.number_of_ratings} />
                            </div>
                        ))}
                    </Flex>
                </Center>
                {showRightArrow && (
                    <ActionIcon
                        variant="filled"
                        color="dark"
                        size="xl"
                        radius="xl"
                        style={{
                            position: 'absolute',
                            right: 0,
                            top: '50%',
                            transform: 'translateY(-50%)',
                            zIndex: 1
                        }}
                        onClick={() => scroll('right')}
                    >
                        <FontAwesomeIcon icon={faChevronRight} />
                    </ActionIcon>
                )}
            </div>
        </Stack>
    )
}