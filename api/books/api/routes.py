from uuid import UUID
from fastapi import APIRouter, Depends

from api.books.api.dependencies import get_book_details_use_case, get_books_use_case, rate_book_use_case, review_book_use_case
from api.books.api.schemas.rate_request import RateRequest
from api.books.api.schemas.review_request import ReviewRequest
from api.users.api.auth import get_current_user


router = APIRouter()

@router.get("/")
async def get_books(get_books=Depends(get_books_use_case), page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc", author_id: UUID = None):
    """
    Get all books.
    """
    books = get_books.execute(page, page_size, sort_by, sort_order, author_id)
    return books

@router.get("/{book_id}")
async def get_book_details(book_id: UUID, get_book_details=Depends(get_book_details_use_case)):
    """
    Get details of a book by its ID.
    """
    book = get_book_details.execute(book_id=book_id)
    return book

@router.post("/{book_id}/rate")
async def rate_book(
        book_id: UUID, 
        rate_request: RateRequest,
        rate_book=Depends(rate_book_use_case), 
        user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    rate_book.execute(book_id=book_id, user_id=user_id, score=rate_request.score)
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
    review_book.execute(book_id=book_id, user_id=user_id, text=review_request.text, score=review_request.score)
    return {"message": "Book reviewed successfully"}

