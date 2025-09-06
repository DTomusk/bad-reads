import { Divider, Stack, Title } from "@mantine/core";
import { useMyBookReviews } from "../hooks/useBooks";
import { Fragment } from "react";
import BookWithReview from "../components/Books/BookWithReview";

export default function UserProfile() {
    const { data: bookReviews } = useMyBookReviews();
    
    return (
        <>
            <Title mt="lg">My Reviews</Title>
            <Divider my="md" />
            <Stack>
                {bookReviews?.map((bookReview) => (
                    <Fragment key={bookReview.book.id}>
                        <BookWithReview {...bookReview} />
                        <Divider my="md" />
                    </Fragment>
                ))}
            </Stack>
        </>
    )
}