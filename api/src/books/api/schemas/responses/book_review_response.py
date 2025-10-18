from typing import List
from pydantic import BaseModel

from src.books.api.schemas.review_response import ReviewResponse
from src.books.domain.models import Review


class BookReviewResponse(BaseModel):
    reviews: List[ReviewResponse]

    @classmethod
    def from_domain(cls, reviews: List[Review]) -> "BookReviewResponse":
        return BookReviewResponse(reviews=[ReviewResponse.from_domain(review) for review in reviews])

