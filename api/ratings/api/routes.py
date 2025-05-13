from uuid import UUID
from fastapi import APIRouter, Depends

from api.ratings.api.dependencies import get_current_user, rate_book_use_case


router = APIRouter()

@router.post("/{book_id}/rate")
async def rate_book(book_id: UUID, rating: float, rate_book=Depends(rate_book_use_case), user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    rate_book.execute(book_id=book_id, user_id=user_id, rating=rating)
    return {"message": "Book rated successfully"}