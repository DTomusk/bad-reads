from uuid import UUID
from src.books.api.schemas.review_response import ReviewResponse
from src.books.domain.models import RatingWithReview
from src.books.application.services.rating_with_review_service import AbstractRatingWithReviewService
from src.books.api.schemas.book_response import BookResponse
from src.books.api.schemas.review_with_book_response import ReviewWithBookResponse
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.application.repositories.book_repository import AbstractBookRepo


class GetBookReviewsForUser():
    def __init__(self, 
                 review_repository: AbstractReviewRepo,
                 book_repository: AbstractBookRepo,
                 rr_service: AbstractRatingWithReviewService):
        self.review_repository = review_repository
        self.book_repository = book_repository
        self.rr_service = rr_service

    def execute(self, user_id: UUID) -> list[ReviewWithBookResponse]:
        reviews = self.review_repository.get_reviews_by_user_id(user_id)
        ratings_with_reviews: list[RatingWithReview] = self.rr_service.get_ratings_with_reviews_from_reviews(reviews)
        rr_responses = [ReviewResponse.from_domain_with_rating_review(rr) for rr in ratings_with_reviews]
        books = self.book_repository.get_books_by_ids([review.book_id for review in reviews])
        book_responses = [BookResponse.from_domain(book) for book in books]
        return [ReviewWithBookResponse.from_domain(review, book) for review, book in zip(rr_responses, book_responses)]