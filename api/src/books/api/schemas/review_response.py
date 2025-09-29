from pydantic import BaseModel, ConfigDict
from src.users.domain.models import User
from src.books.domain.models import Rating, RatingWithReview, Review
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

    # TODO: we might be able to replace this with RatingWithReview?
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
    
    # TODO: ReviewResponse without review makes no sense, consider changing
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
    
    @classmethod
    def from_domain_with_rating_review(cls, rating_with_review: RatingWithReview) -> "ReviewResponse":
        return cls(
            rating_id=rating_with_review.rating_id,
            review_id=rating_with_review.review_id,
            book_id=rating_with_review.book_id,
            user_id=rating_with_review.user_id,
            text=rating_with_review.text,
            date_created=rating_with_review.date_created,
            love_score=rating_with_review.love_score.value,
            shit_score=rating_with_review.shit_score.value
        )
    
class RatingReviewWithUsernameResponse(BaseModel):
    rating_id: UUID
    review_id: UUID | None
    book_id: UUID
    username: str
    text: str
    date_created: datetime.datetime | None
    love_score: float
    shit_score: float

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_domain(cls, rating_review: RatingWithReview, user: User) -> "RatingReviewWithUsernameResponse":
        return cls(
            rating_id=rating_review.rating_id,
            review_id=rating_review.review_id,
            book_id=rating_review.book_id,
            username=user.username.username,
            text=rating_review.text,
            date_created=rating_review.date_created,
            love_score=rating_review.love_score.value,
            shit_score=rating_review.shit_score.value
        )

