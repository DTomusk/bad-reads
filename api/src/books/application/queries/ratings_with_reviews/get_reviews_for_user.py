from uuid import UUID

from ...models import ReviewWithBookDetailsDTO
from ....data.rating_with_review_reader import AbstractRatingWithReviewReader

class GetBookReviewsForUser():
    def __init__(self, 
            rating_with_review_reader: AbstractRatingWithReviewReader):
        self.rating_with_review_reader = rating_with_review_reader

    def execute(self, user_id: UUID) -> list[ReviewWithBookDetailsDTO]:
        return self.rating_with_review_reader.get_reviews_with_ratings_for_user(user_id=user_id)