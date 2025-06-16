from pydantic import BaseModel, ConfigDict
from src.books.domain.models import Rating, Review
from uuid import UUID
import datetime

class ReviewResponse(BaseModel):
    id: UUID
    user_id: UUID
    text: str
    date_created: datetime.datetime
    love_score: float
    shit_score: float

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_domain(cls, review: Review, rating: Rating) -> "ReviewResponse":
        return cls(
            id=review.id,
            user_id=review.user_id,
            text=review.text,
            date_created=review.date_created,
            love_score=rating.love_score.value,
            shit_score=rating.shit_score.value
        )