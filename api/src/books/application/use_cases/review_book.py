from datetime import datetime, timezone
from uuid import UUID, uuid4
from src.books.application.repositories.book_repository import BookRepo
from src.books.application.repositories.rating_repository import RatingRepo
from src.books.application.repositories.review_repository import ReviewRepo
from src.books.domain.models import Rating, RatingScore, Review

# TODO: add a case for updating a review and a case for adding a review to a book that has already been rated
class ReviewBook:
    def __init__(self, book_repository: BookRepo, rating_repository: RatingRepo, review_repository: ReviewRepo):
        self.book_repository = book_repository
        self.rating_repository = rating_repository
        self.review_repository = review_repository

    def execute(self, book_id: UUID, user_id: UUID, text: str, love_score: float, shit_score: float) -> None:
        """ User reviews a book """
        # Check if the book exists
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        # Check if the user has already rated the book
        existing_rating = self.rating_repository.get_rating_by_user_and_book(user_id, book_id)
        if existing_rating:
            raise ValueError("Book already rated by user")
        
        # Check if the user has already reviewed the book
        existing_review = self.review_repository.get_review_by_user_and_book(user_id, book_id)
        if existing_review:
            raise ValueError("Book already reviewed by user")

        # Create a new rating
        new_rating = Rating(uuid4(), book_id, user_id, RatingScore(love_score), RatingScore(shit_score))
        self.rating_repository.create_rating(new_rating)
        book.add_rating(new_rating)
        self.book_repository.update_book(book)

        # Create a new review
        new_review = Review(uuid4(), book_id, user_id, text, new_rating.id, datetime.now(timezone.utc))
        self.review_repository.create_review(new_review)

