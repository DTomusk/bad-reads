from uuid import UUID

# Ratings aren't value objects as they are mutable (should they be?)
# However, Books are the  aggregate root and should be the only entity that can change the ratings
class Rating:
    """ Represents a rating given by a user to a book """
    def __init__(self, id: UUID, book_id: UUID, user_id: UUID, rating: float):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.rating = rating

class Book:
    def __init__(self, id: UUID, title: str, author: str, ratings: list[Rating] = None):
        self.id = id
        self.title = title
        # TODO: author will be its own entity (authors might share names, have descriptions and other data)
        # TODO: should be a list of authors
        self.author = author
        # TODO: will need to track average rating, number of ratings, etc.
        # This can be calculated directly for now, but will need to be stored in the future
        self.ratings = ratings if ratings is not None else []

    def rate(self, user_id: UUID, rating: Rating) -> None:
        """ Rate the book, if the user has already rated it, update the rating """
        existing_rating = next((r for r in self.ratings if r.user_id == user_id), None)
        if existing_rating:
            existing_rating.rating = rating.rating
            return
        self.ratings.append(rating)

    def set_ratings(self, ratings: list[Rating]) -> None:
        """ Set the ratings for the book, for lazy loading or other purposes """
        self.ratings = ratings

    def get_average_rating(self) -> float:
        """ Get the average rating of the book """
        if not self.ratings:
            return 0.0
        return sum(r.rating for r in self.ratings) / len(self.ratings)