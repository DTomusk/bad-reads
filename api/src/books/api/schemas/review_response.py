from pydantic import BaseModel, ConfigDict
from src.books.domain.models import Rating, Review
from uuid import UUID
import datetime

class ReviewResponse(BaseModel):
    rating_id: UUID
    review_id: UUID | None
    book_id: UUID
    user_id: UUID
    text: str
    date_created: datetime.datetime | None
    love_score: float
    shit_score: float

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_domain(cls, review: Review, rating: Rating) -> "ReviewResponse":
        return cls(
            rating_id=rating.id,
            review_id=review.id,
            book_id=review.book_id,
            user_id=review.user_id,
            text=review.text,
            date_created=review.date_created,
            love_score=rating.love_score.value,
            shit_score=rating.shit_score.value
        )
    
    @classmethod
    def from_domain_without_review(cls, rating: Rating) -> "ReviewResponse":
        return cls(
            rating_id=rating.id,
            review_id=None,
            book_id=rating.book_id,
            user_id=rating.user_id,
            text="",
            date_created=None,
            love_score=rating.love_score.value,
            shit_score=rating.shit_score.value
        )