from uuid import UUID
from fastapi import APIRouter
from fastapi.params import Depends

from .dependencies import get_reviews_with_username_reader


router = APIRouter()

@router.get("/books/{book_id}/reviews")
async def get_reviews_with_username(
    book_id: UUID,
    page_size: int = 10,
    page: int = 1,
    sort: str = "newest",
    get_reviews_with_username_reader = Depends(get_reviews_with_username_reader)):
    """
    Gets the reviews for a book and the usernames of the users associated
    """
    return get_reviews_with_username_reader.get_reviews_for_book(book_id=book_id, page_size=page_size, page=page, sort_order=sort)