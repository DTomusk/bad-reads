from fastapi import Depends

from src.books.data.author_repository import AuthorRepo
from src.books.data.book_repository import BookRepo
from src.books.data.rating_repository import RatingRepo
from src.books.data.review_repository import ReviewRepo
from src.infrastructure.db.database import get_session


def get_ratings_repo(session=Depends(get_session)):
    """
    Dependency to provide the Ratings repository.
    """
    return RatingRepo(session=session)

def get_reviews_repo(session=Depends(get_session)):
    """
    Dependency to provide the Reviews repository.
    """
    return ReviewRepo(session=session)

def get_books_repo(session=Depends(get_session)):
    """
    Dependency to provide the Books repository.
    """
    return BookRepo(session=session)

def get_authors_repo(session=Depends(get_session)):
    """
    Dependency to provide the Authors repository.
    """
    return AuthorRepo(session=session)