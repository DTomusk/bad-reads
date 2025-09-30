from fastapi import APIRouter


router = APIRouter()

@router.get("/books/{book_id}/reviews")
async def get_reviews_with_username():
    """
    Gets the reviews for a book and the usernames of the users associated
    """
    pass