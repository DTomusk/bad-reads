import { Box, Flex, Image, Stack, Title, Text } from "@mantine/core";
import { BookWithReviewResponse } from "../../types/bookwithreviewresponse";
import { useNavigate } from "react-router-dom";
import EmojiScoreExpanded from "../Ratings/EmojiScoreExpanded";
import { useBreakpoints } from "../../hooks/useBreakpoints";

export default function BookWithReview({ book, review }: BookWithReviewResponse
) {
    const navigate = useNavigate();
    const {isExtraSmall} = useBreakpoints(); // 48em = Mantine sm breakpoint
    return (
        <Flex gap="md" p="lg" direction={isExtraSmall ? "column" : "row"} align={isExtraSmall ? "center" : "flex-start"}>
            <Box w={isExtraSmall ? "60%" : "20%"}>
                <Image 
                src={book.picture_url} 
                height="100%"
                alt={`${book.title} image`} 
                fit="contain"
                onClick={() => navigate(`/book/${book.id}`)}
                style={{ cursor: "pointer" }}
                />
            </Box>

            <Stack w="80%" style={{ flex: 1 }}>
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
