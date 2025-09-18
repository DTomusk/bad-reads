from uuid import UUID, uuid4

from src.books.application.services.ratings_service import AbstractRatingsService
from src.infrastructure.api.models import Outcome


class CreateRating:
    def __init__(self, rating_service: AbstractRatingsService):
        self.rating_service = rating_service

    def execute(self, book_id: UUID, user_id: UUID, love_score: float, shit_score: float) -> Outcome[UUID]:
        return self.rating_service.create_rating(book_id=book_id, user_id=user_id, love_score=love_score, shit_score=shit_score)
        