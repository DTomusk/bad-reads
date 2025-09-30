from uuid import UUID

from ....users.data.user_repository import AbstractUserRepository

from ....books.data.rating_with_review_reader import AbstractRatingWithReviewReader

from ..models.review_with_username_dto import ReviewWithUsernameDTO


class GetReviewsWithUsernamesForBook:
    def __init__(
            self, 
            rating_with_review_reader: AbstractRatingWithReviewReader,
            user_repo: AbstractUserRepository):
        self.rating_with_review_reader = rating_with_review_reader
        self.user_repo = user_repo

    def execute(self, book_id: UUID) -> ReviewWithUsernameDTO:
        ratings_with_reviews = self.rating_with_review_reader.get_reviews_with_ratings_for_book(book_id=book_id)
        