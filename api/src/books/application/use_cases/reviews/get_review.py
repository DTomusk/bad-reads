from uuid import UUID
from src.books.api.schemas.review_response import ReviewResponse
from src.infrastructure.api.models import Failure, Outcome
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.api.schemas.rating_response import RatingResponse
from src.books.application.repositories.rating_repository import AbstractRatingRepo


class GetReview:
    def __init__(self, review_repo: AbstractReviewRepo, rating_repo: AbstractRatingRepo):
        self.review_repo = review_repo
        self.rating_repo = rating_repo

    def execute(self, book_id: UUID, user_id: UUID) -> Outcome[ReviewResponse]:
        rating = self.rating_repo.get_rating_by_user_and_book(user_id, book_id)

        print(rating)

        if not rating:
            Outcome(isSuccess=False, failure=Failure(error="User has not rated this book"))
        
        review = self.review_repo.get_review_by_rating_id(rating.id)

        print(review)

        if review is None:
            return Outcome(isSuccess=True, data=ReviewResponse.from_domain(rating=rating))
        
        return Outcome(isSuccess=True, data=ReviewResponse.from_domain(review=review, rating=rating))