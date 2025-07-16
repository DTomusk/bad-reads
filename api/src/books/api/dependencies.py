from fastapi import BackgroundTasks, Depends

from src.books.application.use_cases.get_book_reviews import GetBookReviews
from src.infrastructure.services.background_task_queue import FastAPIBackgroundTaskQueue
from src.books.infrastructure.repositories.author_repo import AuthorRepo
from src.books.application.use_cases.search_books import SearchBooks
from src.books.application.use_cases.get_book_details import GetBookDetails
from src.books.application.use_cases.review_book import ReviewBook
from src.books.infrastructure.repositories.review_repo import ReviewRepo
from src.infrastructure.db.database import get_session
from src.books.application.use_cases.get_books import GetBooks
from src.books.application.use_cases.rate_book import RateBook
from src.books.infrastructure.repositories.book_repo import BookRepo
from src.books.infrastructure.repositories.rating_repo import RatingRepo
from src.books.infrastructure.services.google_books_api_service import GoogleBooksApiService

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

def get_external_books_service(author_repo=Depends(get_authors_repo)):
    """
    Dependency to provide the ExternalBooksService.
    """
    return GoogleBooksApiService(author_repo=author_repo)

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

def get_book_details_use_case(book_repo=Depends(get_books_repo)):
    """
    Dependency to provide the GetBookDetails use case.
    """
    return GetBookDetails(book_repository=book_repo)

def search_books_use_case(
    book_repo=Depends(get_books_repo), 
    external_books_service=Depends(get_external_books_service), 
    author_repo=Depends(get_authors_repo), 
    background_tasks: BackgroundTasks = None
):
    """
    Dependency to provide the SearchBooks use case.
    """
    return SearchBooks(
        book_repository=book_repo, 
        external_books_service=external_books_service, 
        author_repository=author_repo, 
        background_task_queue=FastAPIBackgroundTaskQueue(background_tasks=background_tasks)
    )

def get_book_reviews_use_case(review_repo=Depends(get_reviews_repo)):
    """
    Dependency to provide the GetBookReviews use case.
    """
    return GetBookReviews(review_repository=review_repo)