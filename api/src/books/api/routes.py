from uuid import UUID
from fastapi import APIRouter, BackgroundTasks, Depends

from src.books.api.dependencies import get_book_details_use_case, get_book_reviews_use_case, get_books_use_case, rate_book_use_case, review_book_use_case, search_books_use_case
from src.books.api.schemas.book_search_response import BookSearchResponse
from src.books.api.schemas.rate_request import RateRequest
from src.books.api.schemas.review_request import ReviewRequest
from src.users.api.auth import get_current_user


router = APIRouter()

@router.get("/")
async def get_books(
    get_books=Depends(get_books_use_case), 
    page: int = 1, 
    page_size: int = 10, 
    sort_by: str = "title", 
    sort_order: str = "asc", 
    author_id: UUID = None):
    """
    Get all books.
    """
    books = get_books.execute(page, page_size, sort_by, sort_order, author_id)
    return books

@router.get("/search")
async def search_books(
        query: str,
        background_tasks: BackgroundTasks,
        search_books=Depends(search_books_use_case),
        page_size: int = 10,
        page: int = 1) -> BookSearchResponse:
    """
    Search for books by title.
    """
    book_search_response = search_books.execute(query, page_size, page)
    return book_search_response

@router.get("/{book_id}")
async def get_book_details(book_id: UUID, get_book_details=Depends(get_book_details_use_case)):
    """
    Get details of a book by its ID.
    """
    book_details = get_book_details.execute(book_id=book_id)
    return book_details

@router.post("/{book_id}/rate")
async def rate_book(
        book_id: UUID, 
        rate_request: RateRequest,
        rate_book=Depends(rate_book_use_case), 
        user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    rate_book.execute(book_id=book_id, user_id=user_id, love_score=rate_request.love_score, shit_score=rate_request.shit_score)
    return {"message": "Book rated successfully"}

@router.post("/{book_id}/review")
async def review_book(
        book_id: UUID, 
        review_request: ReviewRequest,
        review_book=Depends(review_book_use_case), 
        user_id=Depends(get_current_user)):
    """
    Review a book by its ID.
    """
    review_book.execute(book_id=book_id, user_id=user_id, text=review_request.text, love_score=review_request.love_score, shit_score=review_request.shit_score)
    return {"message": "Book reviewed successfully"}

@router.get("/{book_id}/reviews")
async def get_book_reviews(book_id: UUID, get_book_reviews=Depends(get_book_reviews_use_case)):
    """
    Get reviews of a book by its ID.
    """
    reviews = get_book_reviews.execute(book_id=book_id)
    return reviews


