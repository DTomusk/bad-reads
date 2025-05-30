from dataclasses import dataclass
import datetime
import re
from uuid import UUID

@dataclass(frozen=True)
class RatingScore:
    value: float

    def __post_init__(self):
        if self.value < 0 or self.value > 5:
            raise ValueError("Rating score must be between 0 and 5")

class Rating:
    """ Represents a rating given by a user to a book """
    def __init__(self, id: UUID, book_id: UUID, user_id: UUID, score: RatingScore):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.score = score

# Note: reviews are a superset of ratings
# People can see reviews and interact with them, but not ratings
# Each review must have a rating, but each rating does not have to have a review
class Review:
    """ Represents a review given by a user to a book """
    def __init__(self, id: UUID, book_id: UUID, user_id: UUID, text: str, rating_id: UUID, date_created: datetime):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.text = text
        self.rating_id = rating_id
        self.date_created = date_created
    
class Author:
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name

@dataclass(frozen=True)
class ISBN13:
    value: str

    def __post_init__(self):
        # Remove hyphens or spaces for standardization
        clean_value = re.sub(r'[-\s]', '', self.value)
        if not re.match(r'^\d{13}$', clean_value):
            raise ValueError(f"Invalid ISBN-13 format: {self.value}")

        if not self._is_valid_isbn13(clean_value):
            raise ValueError(f"Invalid ISBN-13 checksum: {self.value}")

        # Set the clean, validated value
        object.__setattr__(self, 'value', clean_value)

    @staticmethod
    def _is_valid_isbn13(isbn: str) -> bool:
        """Validates the ISBN-13 checksum."""
        total = 0
        for i, char in enumerate(isbn[:12]):
            factor = 1 if i % 2 == 0 else 3
            total += int(char) * factor
        check_digit = (10 - (total % 10)) % 10
        return check_digit == int(isbn[12])

    def __str__(self):
        return self.value
        

class Book:
    def __init__(
            self, 
            id: UUID, 
            title: str, 
            authors: list[Author], 
            average_rating: float, 
            number_of_ratings: int,
            sum_of_ratings: float,
            isbn: ISBN13,
            description: str | None = None,
            ):
        self.id = id
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.number_of_ratings = number_of_ratings
        self.sum_of_ratings = sum_of_ratings
        self.isbn = isbn
        self.description = description

    def add_rating(self, rating: Rating) -> None:
        """ Add a rating to the book """
        self.sum_of_ratings += rating.score.value
        self.number_of_ratings += 1
        self.average_rating = self.sum_of_ratings / self.number_of_ratings

    def remove_rating(self, rating: Rating) -> None:
        """ Remove a rating from the book """
        self.sum_of_ratings -= rating.score.value
        self.number_of_ratings -= 1
        if self.number_of_ratings > 0:
            self.average_rating = self.sum_of_ratings / self.number_of_ratings
        else:
            self.average_rating = 0

    def update_rating(self, old_rating: Rating, new_rating: Rating) -> None:
        """ Update a rating for the book """
        self.remove_rating(old_rating)
        self.add_rating(new_rating)
