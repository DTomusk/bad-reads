from fastapi import BackgroundTasks, Depends

from src.books.application.use_cases.reviews.get_review import GetReview
from src.books.application.use_cases.reviews.update_review import UpdateReview
from src.books.application.use_cases.ratings.update_rating import UpdateRating
from src.shared.api.dependencies import get_profanity_service
from src.books.application.services.ratings_service import RatingsService
from src.books.api.dependencies.repos import get_authors_repo, get_books_repo, get_ratings_repo, get_reviews_repo
from src.books.application.use_cases.reviews.get_reviews_for_user import GetBookReviewsForUser
from src.books.application.use_cases.reviews.get_reviews_for_book import GetBookReviews
from src.infrastructure.services.background_task_queue import FastAPIBackgroundTaskQueue
from src.books.application.use_cases.books.search_books import SearchBooks
from src.books.application.use_cases.books.get_book_details import GetBookDetails
from src.books.application.use_cases.reviews.create_review import CreateReview
from src.books.application.use_cases.books.get_books import GetBooks
from src.books.application.use_cases.ratings.create_rating import CreateRating
from src.books.application.services.external_books_service import GoogleBooksApiService
from src.books.application.use_cases.ratings.get_rating_for_book_for_user import GetRatingForBookForUser

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

def create_rating_use_case(rating_service=Depends(get_rating_service)):
    """
    Dependency to provide the CreateRating use case.
    """
    return CreateRating(rating_service=rating_service)

def update_rating_use_case(rating_service=Depends(get_rating_service), rating_repo=Depends(get_ratings_repo)):
    """
    Dependency to provide the CreateRating use case.
    """
    return UpdateRating(rating_service=rating_service, rating_repo=rating_repo)

def get_review_use_case(review_repo=Depends(get_reviews_repo), rating_repo=Depends(get_ratings_repo)):
    return GetReview(review_repo=review_repo, rating_repo=rating_repo)

def create_review_use_case(rating_service=Depends(get_rating_service), review_repo=Depends(get_reviews_repo), profanity_service=Depends(get_profanity_service)):
    """
    Dependency to provide the CreateReview use case.
    """
    return CreateReview(rating_service=rating_service, review_repository=review_repo, profanity_service=profanity_service)

def update_review_use_case(rating_service=Depends(get_rating_service), review_repo=Depends(get_reviews_repo), rating_repo=Depends(get_ratings_repo), profanity_service=Depends(get_profanity_service)):
    """
    Dependency to provide the UpdateReview use case.
    """
    return UpdateReview(rating_service=rating_service, rating_repository=rating_repo, review_repository=review_repo, profanity_service=profanity_service)

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

def get_book_rating_use_case(rating_repo=Depends(get_ratings_repo)):
    """
    Dependency to provide the GetBookRating use case.
    """
    return GetRatingForBookForUser(rating_repository=rating_repo)

def get_book_reviews_use_case(review_repo=Depends(get_reviews_repo)):
    """
    Dependency to provide the GetBookReviews use case.
    """
    return GetBookReviews(review_repository=review_repo)

def get_my_book_reviews_use_case(review_repo=Depends(get_reviews_repo), book_repo=Depends(get_books_repo)):
    """
    Dependency to provide the GetBooReviewsForUser use case.
    """
    return GetBookReviewsForUser(review_repository=review_repo, book_repository=book_repo)
