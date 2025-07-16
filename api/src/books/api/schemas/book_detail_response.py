from pydantic import BaseModel
from src.books.domain.models import Book

class BookDetailResponse(BaseModel):
    id: str
    title: str
    authors: list[str]
    average_love_rating: float
    average_shit_rating: float
    number_of_ratings: int
    sum_of_love_ratings: float
    sum_of_shit_ratings: float
    picture_url: str | None
    description: str

    @classmethod
    def from_domain(cls, book: Book) -> "BookDetailResponse":
        return cls(
            id=str(book.id),
            title=book.title,
            authors=[author.name for author in book.authors],
            average_love_rating=book.average_love_rating if book.average_love_rating else 0,
            average_shit_rating=book.average_shit_rating if book.average_shit_rating else 0,
            number_of_ratings=book.number_of_ratings if book.number_of_ratings else 0,
            sum_of_love_ratings=book.sum_of_love_ratings if book.sum_of_love_ratings else 0,
            sum_of_shit_ratings=book.sum_of_shit_ratings if book.sum_of_shit_ratings else 0,
            picture_url=book.picture_url if book.picture_url else "",
            description=book.description if book.description else "No description available",
        )