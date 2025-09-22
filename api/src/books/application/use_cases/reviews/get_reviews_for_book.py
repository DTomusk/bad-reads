from uuid import UUID
from src.books.application.services.rating_with_review_service import AbstractRatingWithReviewService
from src.books.domain.models import RatingWithReview, Review
from src.users.application.repositories.user_repository import AbstractUserRepository
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.api.schemas.review_response import RatingReviewWithUsernameResponse, ReviewResponse

class GetBookReviews():
    def __init__(
            self, 
            review_repository: AbstractReviewRepo, 
            user_repo: AbstractUserRepository,
            rating_with_review_service: AbstractRatingWithReviewService):
        self.review_repository = review_repository
        self.user_repo = user_repo
        self.rating_with_review_serivce = rating_with_review_service

    def execute(self, book_id: UUID, sort: str) -> list[RatingReviewWithUsernameResponse]:
        # TODO: use case shouldn't know about sort syntax
        if sort == "newest":
            sort_by = "date_created"
            sort_order = "desc"
        elif sort == "oldest":
            sort_by = "date_created"
            sort_order = "asc"
        else:
            raise ValueError(f"Invalid sort order: {sort}")
        
        reviews: list[Review] = self.review_repository.get_reviews_by_book_id(book_id, sort_by, sort_order)

        ratings_with_reviews: list[RatingWithReview] = self.rating_with_review_serivce.get_ratings_with_reviews_from_reviews(reviews)

        if ratings_with_reviews == []:
            return []

        user_details = self.user_repo.get_by_ids([review.id for review in reviews])

        response: list[RatingReviewWithUsernameResponse] = []

        for rr in ratings_with_reviews:
            user = user_details.get(rr.user_id)
            if user is None:
                raise ValueError("Couldn't find user for rating")
            result = RatingReviewWithUsernameResponse.from_domain(rating_review=rr, user=user)
            response.append(result)

        return response
            
