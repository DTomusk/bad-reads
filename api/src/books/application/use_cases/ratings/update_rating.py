from uuid import UUID

from src.books.domain.models import Rating, RatingScore
from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.books.application.services.ratings_service import AbstractRatingsService
from src.infrastructure.api.models import Failure, Outcome


class UpdateRating:
    def __init__(self, rating_service: AbstractRatingsService, rating_repo: AbstractRatingRepo):
        self.rating_service = rating_service
        self.rating_repo = rating_repo

    def execute(self, rating_id: UUID, book_id: UUID, user_id: UUID, love_score: float, shit_score: float) -> Outcome[UUID]:
        # TODO: get rating for ID 
        existing_rating = self.rating_repo.get_rating_by_id(rating_id)
        if existing_rating is None:
            return Outcome(isSuccess=False, failure=Failure(error="A rating with this ID doesn't exist"))
        
        if existing_rating.book_id != book_id:
            return Outcome(isSuccess=False, failure=Failure(error="The rating to be updated isn't for the same book as the one requested"))
        
        if existing_rating.user_id != user_id:
            return Outcome(isSuccess=False, failure=Failure(error="Can't change another user's rating"))
        
        new_rating = Rating(rating_id, book_id, user_id, RatingScore(love_score), RatingScore(shit_score))

        return self.rating_service.update_rating(book_id=book_id, old_rating=existing_rating, new_rating=new_rating)
        