from fastapi import BackgroundTasks, Depends

from ...application.queries.books.get_book_details import GetBookDetails
from ...application.queries.books.get_books import GetBooks
from ...application.queries.books.search_books import SearchBooks
from ...application.queries.ratings_with_reviews.get_reviews_for_user import GetBookReviewsForUser
from ...application.queries.ratings_with_reviews.get_review_for_book_for_user import GetReview

from ...application.commands.create_rating import CreateRating

from ...application.services.ratings_service import RatingsService
from ...application.services.external_books_service import GoogleBooksApiService

from ..dependencies.data import get_authors_repo, get_books_repo, get_rating_with_review_reader, get_ratings_repo, get_reviews_repo
from ....infrastructure.services.background_task_queue import FastAPIBackgroundTaskQueue

# TODO: split out use cases once there are too many of them
def get_external_books_service(author_repo=Depends(get_authors_repo)):
    """
    Dependency to provide the ExternalBooksService.
    """
    return GoogleBooksApiService(author_repo=author_repo)

def get_rating_service(
        rating_repository=Depends(get_ratings_repo), 
        book_repository=Depends(get_books_repo),
        background_tasks: BackgroundTasks = None
    ):
    """
    Dependency to provide the RatingService.
    """
    return RatingsService(
        rating_repository=rating_repository,
        book_repository=book_repository,
        background_task_queue=FastAPIBackgroundTaskQueue(background_tasks=background_tasks))

def create_rating_use_case(rating_service=Depends(get_rating_service), rating_repo=Depends(get_ratings_repo), review_repo=Depends(get_reviews_repo)):
    """
    Dependency to provide the CreateRating use case.
    """
    return CreateRating(rating_service=rating_service, rating_repo=rating_repo, review_repo=review_repo)

def get_review_use_case(rating_with_review_reader=Depends(get_rating_with_review_reader)):
    return GetReview(rating_with_review_reader=rating_with_review_reader)

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

def get_my_book_reviews_use_case(review_repo=Depends(get_reviews_repo), book_repo=Depends(get_books_repo)):
    """
    Dependency to provide the GetBooReviewsForUser use case.
    """
    return GetBookReviewsForUser(review_repository=review_repo, book_repository=book_repo)
