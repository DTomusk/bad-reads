from uuid import UUID, uuid4
from fastapi import Depends

from src.books.application.use_cases.get_book_details import GetBookDetails
from src.books.application.use_cases.review_book import ReviewBook
from src.books.infrastructure.repositories.sqlite_review_repo import SqliteReviewRepo
from src.infrastructure.db.database import get_session
from src.books.application.use_cases.get_books import GetBooks
from src.books.application.use_cases.rate_book import RateBook
from src.books.infrastructure.repositories.sqlite_book_repo import SqliteBookRepo
from src.books.infrastructure.repositories.sqlite_rating_repo import SqliteRatingRepo
        

def get_ratings_repo(session=Depends(get_session)):
    """
    Dependency to provide the Ratings repository.
    """
    return SqliteRatingRepo(session=session)

def get_reviews_repo(session=Depends(get_session)):
    """
    Dependency to provide the Reviews repository.
    """
    return SqliteReviewRepo(session=session)

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

def review_book_use_case(book_repo=Depends(get_books_repo), rating_repo=Depends(get_ratings_repo), review_repo=Depends(get_reviews_repo)):
    """
    Dependency to provide the ReviewBook use case.
    """
    return ReviewBook(book_repository=book_repo, rating_repository=rating_repo, review_repository=review_repo)

def get_books_use_case(book_repo=Depends(get_books_repo)):
    """
    Dependency to provide the GetBooks use case.
    """
    return GetBooks(book_repository=book_repo)

def get_book_details_use_case(book_repo=Depends(get_books_repo), rating_repo=Depends(get_ratings_repo)):
    """
    Dependency to provide the GetBookDetails use case.
    """
    return GetBookDetails(book_repository=book_repo, rating_repository=rating_repo)