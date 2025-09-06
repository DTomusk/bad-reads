import { Box, Flex, Image, Stack, Title, Text } from "@mantine/core";
import { BookWithReviewResponse } from "../../types/bookwithreviewresponse";
import { useNavigate } from "react-router-dom";
import EmojiScoreExpanded from "../Ratings/EmojiScoreExpanded";

export default function BookWithReview({ book, review }: BookWithReviewResponse
) {
    const navigate = useNavigate();
    return (
        <Flex gap="md" p="lg">
            <Box>
                <Image 
                src={book.picture_url} 
                height="100%"
                alt={`${book.title} image`} 
                fit="contain"
                onClick={() => navigate(`/book/${book.id}`)}
                style={{ cursor: "pointer" }}
                />
            </Box>

            <Stack w="100%" style={{ flex: 1 }}>
                <Title order={2} onClick={() => navigate(`/book/${book.id}`)} 
          className="hover-underline">{book.title}</Title>
                <EmojiScoreExpanded 
                    love_score={review.love_score} 
                    shit_score={review.shit_score} 
                    align="left"
                    size="small"
                    hide_number_of_ratings={true}
                    stacked={false}
                    />
                <Text style={{ overflowWrap: "break-word"}}>
                    {review.text}
                </Text>
            </Stack>
        </Flex>
    )
}
