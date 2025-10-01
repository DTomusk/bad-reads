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

    # TODO: it might be simpler to read all the data in one db query 
    # It's not like the user and book datastores are going to be different any time soon
    def execute(self, book_id: UUID) -> ReviewWithUsernameDTO:
        ratings_with_reviews = self.rating_with_review_reader.get_reviews_with_ratings_for_book(book_id=book_id)
        if len(ratings_with_reviews) == 0:
            return []
        
        user_ids = [rating.user_id for rating in ratings_with_reviews]
        user_details = self.user_repo.get_by_ids(user_ids=user_ids)

        return [ReviewWithUsernameDTO(
            love_score=rating.love_score,
            shit_score=rating.shit_score,
            text=rating.text,
            date_created=rating.date_created,
            username=user_details[rating.user_id].username.username) for rating in ratings_with_reviews]

