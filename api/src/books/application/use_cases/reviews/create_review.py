from datetime import datetime, timezone
from uuid import UUID, uuid4
from src.shared.application.profanity_service import AbstractProfanityService
from src.books.application.services.ratings_service import AbstractRatingsService
from src.infrastructure.api.models import Failure, Outcome
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.domain.models import Review

# TODO: add a case for updating a review and a case for adding a review to a book that has already been rated
class CreateReview:
    def __init__(self, rating_service: AbstractRatingsService, review_repository: AbstractReviewRepo, profanity_service: AbstractProfanityService):
        self.rating_service = rating_service
        self.review_repository = review_repository
        self.profanity_service = profanity_service

    def execute(self, book_id: UUID, user_id: UUID, text: str, love_score: float, shit_score: float) -> Outcome[None]:
        """ User reviews a book """
        existing_review = self.review_repository.get_review_by_user_and_book(user_id, book_id)
        if existing_review:
            return Outcome(isSuccess=False, failure="Book already rated by user")
        
        if self.profanity_service.string_contains_profanity(text):
            return Outcome(isSuccess=False, failure=Failure(error="Review contains profanity"))

        rating_outcome: Outcome[UUID] = self.rating_service.create_rating(book_id=book_id, user_id=user_id, love_score=love_score, shit_score=shit_score)

        if not rating_outcome.isSuccess:
            return rating_outcome
        
        rating_id = rating_outcome.data

        # Create a new review
        new_review = Review(uuid4(), book_id, user_id, text, rating_id)
        self.review_repository.create_review(new_review)

        return Outcome(isSuccess=True)

