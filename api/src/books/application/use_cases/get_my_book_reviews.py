from uuid import UUID
from src.books.api.schemas.book_response import BookResponse
from src.books.api.schemas.review_with_book_response import ReviewWithBookResponse
from src.books.application.repositories.review_repository import AbstractReviewRepo
from src.books.application.repositories.book_repository import AbstractBookRepo


class GetMyBookReviews():
    def __init__(self, 
                 review_repository: AbstractReviewRepo,
                 book_repository: AbstractBookRepo):
        self.review_repository = review_repository
        self.book_repository = book_repository

    def execute(self, user_id: UUID) -> list[ReviewWithBookResponse]:
        reviews = self.review_repository.get_reviews_by_user_id(user_id)
        books = self.book_repository.get_books_by_ids([review.book_id for review in reviews])
        book_responses = [BookResponse.from_domain(book) for book in books]
        return [ReviewWithBookResponse.from_domain(review, book) for review, book in zip(reviews, book_responses)]