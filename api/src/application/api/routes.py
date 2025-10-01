from uuid import UUID
from fastapi import APIRouter
from fastapi.params import Depends

from .dependencies import get_reviews_with_username_query


router = APIRouter()

@router.get("/books/{book_id}/reviews")
async def get_reviews_with_username(
    book_id: UUID,
    get_reviews_with_username_query = Depends(get_reviews_with_username_query)):
    """
    Gets the reviews for a book and the usernames of the users associated
    """
    return get_reviews_with_username_query.execute(book_id=book_id)