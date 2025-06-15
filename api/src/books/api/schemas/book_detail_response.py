from pydantic import BaseModel
from src.books.api.schemas.review_response import ReviewResponse
from src.books.domain.models import Book

class BookDetailResponse(BaseModel):
    title: str
    authors: list[str]
    average_love_rating: float
    average_shit_rating: float
    number_of_ratings: int
    sum_of_love_ratings: float
    sum_of_shit_ratings: float

    reviews: list[ReviewResponse]

    @classmethod
    def from_domain(cls, book: Book, reviews: list[ReviewResponse]) -> "BookDetailResponse":
        return cls(
            title=book.title,
            authors=[author.name for author in book.authors],
            average_love_rating=book.average_love_rating,
            average_shit_rating=book.average_shit_rating,
            number_of_ratings=book.number_of_ratings,
            sum_of_love_ratings=book.sum_of_love_ratings,
            sum_of_shit_ratings=book.sum_of_shit_ratings,
            reviews=reviews)