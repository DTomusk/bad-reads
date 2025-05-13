from uuid import UUID, uuid4
from fastapi import Depends

from api.infrastructure.db.database import get_session
from api.ratings.application.use_cases.rate_book import RateBook
from api.ratings.infrastructure.repositories.sqlite_book_repo import SqliteBookRepo
from api.ratings.infrastructure.repositories.sqlite_rating_repo import SqliteRatingRepo


def get_ratings_repo(session=Depends(get_session)):
    """
    Dependency to provide the Ratings repository.
    """
    return SqliteRatingRepo(session=session)

def get_books_repo(session=Depends(get_session)):
    """
    Dependency to provide the Books repository.
    """
    return SqliteBookRepo(session=session)

def rate_book_use_case(book_repo=Depends(get_books_repo), rating_repo=Depends(get_ratings_repo)):
    """
    Dependency to provide the RateBook use case.
    """
    return RateBook(book_repository=book_repo, rating_repository=rating_repo)

def get_current_user():
    # Mocking this until we have users
    return UUID("5bf2b03f-f375-44a4-93e9-3603e991178f") 