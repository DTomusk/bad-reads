from uuid import UUID

from ....data.rating_with_review_reader import AbstractRatingWithReviewReader
from ...models import RatingWithReviewDTO

class GetReviewForBookForUser:
    def __init__(self, rating_with_review_reader: AbstractRatingWithReviewReader):
        self.rating_with_review_reader = rating_with_review_reader

    def execute(self, book_id: UUID, user_id: UUID) -> RatingWithReviewDTO:
        return self.rating_with_review_reader.get_rating_with_review_for_user_and_book(book_id=book_id, user_id=user_id)