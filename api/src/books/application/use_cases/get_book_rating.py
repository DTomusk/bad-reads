from uuid import UUID
from src.books.api.schemas.rating_response import RatingResponse
from src.books.application.repositories.rating_repository import AbstractRatingRepo


class GetBookRating:
    def __init__(self, rating_repository: AbstractRatingRepo):
        self.rating_repository = rating_repository

    def execute(self, book_id: UUID, user_id: UUID) -> RatingResponse:
        rating = self.rating_repository.get_rating_by_user_and_book(user_id, book_id)
        if not rating:
            return None
        return RatingResponse(love_score=rating.love_score.value, shit_score=rating.shit_score.value)