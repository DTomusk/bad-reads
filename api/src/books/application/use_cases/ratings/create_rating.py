from typing import Optional
from uuid import UUID, uuid4

from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.domain.models import Rating, RatingScore, Review
from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.books.application.services.ratings_service import AbstractRatingsService
from src.infrastructure.api.models import Outcome


class CreateRating:
    def __init__(self, rating_service: AbstractRatingsService, rating_repo: AbstractRatingRepo, review_repo: AbstractReviewRepo):
        self.rating_service = rating_service
        self.rating_repo = rating_repo
        self.review_repo = review_repo

    def execute(self, book_id: UUID, user_id: UUID, love_score: float, shit_score: float, text: str = None) -> Outcome[UUID]:
        existing_rating = self.rating_repo.get_rating_by_user_and_book(user_id=user_id, book_id=book_id)
        if existing_rating is None:
            return self._handle_new_rating(book_id=book_id, user_id=user_id, love_score=love_score, shit_score=shit_score, text=text)
        else:
            return self._handle_existing_rating(existing_rating=existing_rating, book_id=book_id, user_id=user_id, love_score=love_score, shit_score=shit_score, text=text)
        
    def _handle_new_rating(self, book_id: UUID, user_id: UUID, love_score: float, shit_score: float, text: str = None) -> Outcome[UUID]:
        outcome: Outcome[UUID] = self.rating_service.create_rating(book_id=book_id, user_id=user_id, love_score=love_score, shit_score=shit_score)

        # If we failed to create a rating, or there is nothing left to do (no review), then return 
        if not outcome.isSuccess or not text:
            return outcome
        
        # TODO: we should have some kind of transaction that if we create a rating but fail to create a review, we roll back the rating
        # Do we need that? 
        review = Review(id=uuid4(), book_id=book_id, user_id=user_id, text=text, rating_id=outcome.data)
        self.review_repo.create_review(review)

        return outcome

    def _handle_existing_rating(self, existing_rating: Rating, book_id: UUID, user_id: UUID, love_score: float, shit_score: float, text: str = None) -> Outcome[UUID]:
        updated_rating = Rating(id=existing_rating.id, book_id=book_id, user_id=user_id, love_score=RatingScore(love_score), shit_score=RatingScore(shit_score))
        if existing_rating.love_score.value != updated_rating.love_score.value or existing_rating.shit_score.value != updated_rating.shit_score.value:
            update_outcome = self.rating_service.update_rating(book_id=book_id, old_rating=existing_rating, new_rating=updated_rating)

            if not update_outcome.isSuccess:
                return update_outcome

        existing_review = self.review_repo.get_review_by_rating_id(existing_rating.id)

        # If there is no review to update and no review update to make, return
        if not text and not existing_review:
            return Outcome(isSuccess=True, data=existing_rating.id)
        
        if not text and existing_review: 
            # delete review (soft)
            self.review_repo.delete_review(existing_review.id)
            return Outcome(isSuccess=True, data=existing_rating.id)

        if text and not existing_review:
            # create new review 
            review = Review(id=uuid4(), book_id=book_id, user_id=user_id, text=text, rating_id=existing_rating.id)
            self.review_repo.create_review(review)
            return Outcome(isSuccess=True, data=existing_rating.id)

        # update an existing review 
        self.review_repo.update_review(review_id=existing_review.id, text=text)
        return Outcome(isSuccess=True, data=existing_rating.id)

        
        
