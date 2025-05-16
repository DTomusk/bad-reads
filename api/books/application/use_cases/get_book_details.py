from uuid import UUID
from api.books.application.repositories.book_repository import BookRepo
from api.books.application.repositories.rating_repository import RatingRepo


class GetBookDetails:
    def __init__(self, book_repository: BookRepo, rating_repository: RatingRepo):
        self.book_repository = book_repository
        self.rating_repository = rating_repository

    def execute(self, book_id: UUID):
        """ Get book details by its ID """
        # Get the book details
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        return book

        # # Get the ratings for the book
        # ratings = self.rating_repository.get_ratings_by_book_id(book_id)

        # # Calculate the average rating
        # average_rating = sum(rating.rating for rating in ratings) / len(ratings) if ratings else 0

        # return {
        #     "book": book,
        #     "average_rating": average_rating,
        #     "ratings": ratings,
        # }