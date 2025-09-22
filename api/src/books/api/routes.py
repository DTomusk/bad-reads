from uuid import UUID
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.params import Query

from src.books.application.use_cases.books.search_books import SearchBooks
from src.books.application.use_cases.books.get_books import GetBooks
from src.books.application.use_cases.reviews.get_reviews_for_book import GetBookReviews
from src.books.api.schemas.book_sort_options import BookSortOption
from src.books.api.schemas.book_detail_response import BookDetailResponse
from src.books.domain.models import Book
from src.infrastructure.api.models import Outcome
from src.books.api.dependencies.application import create_rating_use_case, get_book_details_use_case, get_book_rating_use_case, get_book_reviews_use_case, get_books_use_case, get_my_book_reviews_use_case, get_review_use_case, search_books_use_case
from src.books.api.schemas.book_search_response import BookSearchResponse
from src.books.api.schemas.rating_request import RatingRequest
from src.users.api.auth import get_current_user


router = APIRouter()

@router.get("/")
async def get_books(
    get_books: GetBooks = Depends(get_books_use_case), 
    page: int = 1, 
    page_size: int = 10, 
    sort_by: BookSortOption = Query(BookSortOption.alphabetical, description="Sorting option"), 
    sort_order: str = "asc"):
    """
    Get all books.
    """
    books = get_books.execute(page, page_size, sort_by, sort_order)
    return books

@router.get("/search")
async def search_books(
        query: str,
        background_tasks: BackgroundTasks,
        search_books: SearchBooks = Depends(search_books_use_case),
        page_size: int = 10,
        page: int = 1) -> BookSearchResponse:
    """
    Search for books by title.
    """
    book_search_response = search_books.execute(query, page_size, page)
    return book_search_response

@router.get("/my-reviews")
async def get_my_book_reviews(
    get_my_book_reviews=Depends(get_my_book_reviews_use_case),
    user_id: str = Depends(get_current_user)):
    """
    Get reviews of books by the current user.
    """
    reviews = get_my_book_reviews.execute(user_id=user_id)
    return reviews

@router.get("/{book_id}")
async def get_book_details(
    book_id: UUID, 
    get_book_details=Depends(get_book_details_use_case)):
    """
    Get details of a book by its ID.
    """
    book_details: Outcome[Book] = get_book_details.execute(book_id=book_id)

    if not book_details.isSuccess:
        raise HTTPException(status_code=book_details.failure.code, detail=book_details.failure.error)
    
    response: BookDetailResponse = BookDetailResponse.from_domain(book_details.data)

    return response

@router.get("/{book_id}/rating")
async def get_book_rating(
    book_id: UUID, 
    get_book_rating=Depends(get_book_rating_use_case), 
    user_id=Depends(get_current_user)):
    """
    Get rating of a book by its ID.
    """
    book_rating = get_book_rating.execute(book_id=book_id, user_id=user_id)
    return book_rating

# Catch-all endpoint for creating and updating ratings and reviews 
# TODO: test this out and see if it's a good idea
@router.post("/{book_id}/rate")
async def rate_book(
        background_tasks: BackgroundTasks,
        book_id: UUID, 
        rate_request: RatingRequest,
        rate_book=Depends(create_rating_use_case), 
        user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    outcome: Outcome = rate_book.execute(book_id=book_id, user_id=user_id, love_score=rate_request.love_score, shit_score=rate_request.shit_score, text=rate_request.text)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)

@router.get("/{book_id}/reviews")
async def get_book_reviews(
    book_id: UUID, 
    sort: str = "newest", 
    get_book_reviews: GetBookReviews =Depends(get_book_reviews_use_case)):
    """
    Get reviews of a book by its ID.
    """
    reviews = get_book_reviews.execute(book_id=book_id, sort=sort)
    return reviews

@router.get("/{book_id}/user-rating")
async def get_rating_for_user(
    book_id: UUID,
    get_review=Depends(get_review_use_case),
    user_id=Depends(get_current_user)):
    outcome: Outcome = get_review.execute(book_id, user_id)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)

    return outcome.data