from pydantic import BaseModel

from src.books.api.schemas.book_response import BookResponse
from src.books.api.schemas.review_response import ReviewResponse


class ReviewWithBookResponse(BaseModel):
    review: ReviewResponse
    book: BookResponse

    @classmethod
    def from_domain(cls, review: ReviewResponse, book: BookResponse) -> "ReviewWithBookResponse":
        return cls(review=review, book=book)