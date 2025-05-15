from uuid import UUID, uuid4

from api.ratings.application.repositories.book_repository import BookRepo
from api.ratings.application.repositories.rating_repository import RatingRepo
from api.ratings.domain.models import Rating


class RateBook:
    def __init__(self, book_repository: BookRepo, rating_repository: RatingRepo):
        self.book_repository = book_repository
        self.rating_repository = rating_repository

    def execute(self, book_id: UUID, user_id: UUID, rating: float) -> None:
        """ Rate a book by a user """
        # Check if the book exists
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        # Check if the user has already rated the book
        # this should return a Rating object or None
        existing_rating = self.rating_repository.get_rating_by_user_and_book(user_id, book_id)
        if existing_rating:
            existing_rating.rating = rating
            self.rating_repository.update_rating(existing_rating)
        else:
            new_rating = Rating(uuid4(), book_id, user_id, rating)
            self.rating_repository.create_rating(new_rating)
        # Update the book's ratings
        book.rate(user_id, rating)
        # TODO: consider how we store the book's ratings
        # although we want to access ratings through the book
        # we can still handle them independently

        # Save changes to the book in the repository
        # self.book_repository.update_book(book)