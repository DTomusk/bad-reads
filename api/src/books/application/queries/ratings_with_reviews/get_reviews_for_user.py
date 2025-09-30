from uuid import UUID

from ...models.rating_with_review_dto import RatingWithReviewDTO
from ....data.rating_with_review_reader import AbstractRatingWithReviewReader

class GetBookReviewsForUser():
    def __init__(self, 
                 rating_with_review_reader: AbstractRatingWithReviewReader):
        self.rating_with_review_reader = rating_with_review_reader

    def execute(self, user_id: UUID) -> list[RatingWithReviewDTO]:
        return self.rating_with_review_reader.get_review_with_rating_for_user(user_id=user_id)