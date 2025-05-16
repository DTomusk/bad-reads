from uuid import UUID
from fastapi import APIRouter, Depends

from api.books.api.dependencies import get_book_details_use_case, get_books_use_case, rate_book_use_case
from api.users.api.auth import get_current_user


router = APIRouter()

@router.get("/")
async def get_books(get_books=Depends(get_books_use_case)):
    """
    Get all books.
    """
    books = get_books.execute()
    return books

@router.get("/{book_id}")
async def get_book_details(book_id: UUID, get_book_details=Depends(get_book_details_use_case)):
    """
    Get details of a book by its ID.
    """
    book = get_book_details.execute(book_id=book_id)
    return book

@router.post("/{book_id}/rate")
async def rate_book(book_id: UUID, score: float, rate_book=Depends(rate_book_use_case), user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    rate_book.execute(book_id=book_id, user_id=user_id, score=score)
    return {"message": "Book rated successfully"}