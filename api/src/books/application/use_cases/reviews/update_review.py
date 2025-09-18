from datetime import datetime, timezone
from uuid import UUID, uuid4
from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.shared.application.profanity_service import AbstractProfanityService
from src.books.application.services.ratings_service import AbstractRatingsService
from src.infrastructure.api.models import Failure, Outcome
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.domain.models import Rating, RatingScore, Review

# TODO: add a case for updating a review and a case for adding a review to a book that has already been rated
class UpdateReview:
    def __init__(self, 
            rating_service: AbstractRatingsService, 
            review_repository: AbstractReviewRepo, 
            rating_repository: AbstractRatingRepo,
            profanity_service: AbstractProfanityService):
        self.rating_service = rating_service
        self.review_repository = review_repository
        self.rating_repository = rating_repository
        self.profanity_service = profanity_service

    def execute(self, review_id: UUID, book_id: UUID, user_id: UUID, text: str, love_score: float, shit_score: float) -> Outcome[None]:
        """ User reviews a book """
        existing_review = self.review_repository.get_review_by_id(review_id)
        if existing_review is None:
            return Outcome(isSuccess=False, failure="There is no review to update")
        
        if existing_review.book_id != book_id:
            return Outcome(isSuccess=False, failure="Invalid request, book id for existing review does not match the one supplied")
        
        if existing_review.user_id != user_id:
            return Outcome(isSuccess=False, failure="Requested review to update is not the current user's")

        if self.profanity_service.string_contains_profanity(text):
            return Outcome(isSuccess=False, failure=Failure(error="Review contains profanity"))
        
        existing_rating = self.rating_repository.get_rating_by_id(existing_review.rating_id)

        if existing_rating is None: 
            return Outcome(isSuccess=False, failure="There is no rating associated with this review")
        
        # If the score is any different, udpate the rating (this updates some global stuff too), otherwise don't 
        if love_score != existing_rating.love_score and shit_score != existing_rating.shit_score:
            new_rating = Rating(existing_rating.id, book_id=book_id, user_id=user_id, love_score=RatingScore(love_score), shit_score=RatingScore(shit_score))
            rating_outcome: Outcome[UUID] = self.rating_service.update_rating(book_id=book_id, old_rating=existing_rating, new_rating=new_rating)

            if not rating_outcome.isSuccess:
                return rating_outcome
            
        # update the text of the review 

        # Create a new review
        self.review_repository.update_review(review_id=review_id, text=text)

        return Outcome(isSuccess=True)

