from uuid import UUID
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.params import Query

from src.books.api.schemas.book_sort_options import BookSortOption
from src.books.api.schemas.book_detail_response import BookDetailResponse
from src.books.domain.models import Book
from src.infrastructure.api.models import Outcome
from src.books.api.dependencies.application import create_rating_use_case, create_review_use_case, get_book_details_use_case, get_book_rating_use_case, get_book_reviews_use_case, get_books_use_case, get_my_book_reviews_use_case, get_review_use_case, search_books_use_case, update_rating_use_case, update_review_use_case
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
        search_books=Depends(search_books_use_case),
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
    user_id=Depends(get_current_user)):
    """
    Get reviews of books by the current user.
    """
    reviews = get_my_book_reviews.execute(user_id=user_id)
    return reviews

@router.get("/{book_id}")
async def get_book_details(book_id: UUID, get_book_details=Depends(get_book_details_use_case)):
    """
    Get details of a book by its ID.
    """
    book_details: Outcome[Book] = get_book_details.execute(book_id=book_id)

    if not book_details.isSuccess:
        raise HTTPException(status_code=book_details.failure.code, detail=book_details.failure.error)
    
    response: BookDetailResponse = BookDetailResponse.from_domain(book_details.data)

    return response

@router.get("/{book_id}/rating")
async def get_book_rating(book_id: UUID, get_book_rating=Depends(get_book_rating_use_case), user_id=Depends(get_current_user)):
    """
    Get rating of a book by its ID.
    """
    book_rating = get_book_rating.execute(book_id=book_id, user_id=user_id)
    return book_rating

@router.post("/{book_id}/rate")
async def rate_book(
        background_tasks: BackgroundTasks,
        book_id: UUID, 
        rate_request: RateRequest,
        rate_book=Depends(create_rating_use_case), 
        user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    outcome: Outcome = rate_book.execute(book_id=book_id, user_id=user_id, love_score=rate_request.love_score, shit_score=rate_request.shit_score)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)
    
@router.post("/{book_id}/rate/{rating_id}/update")
async def update_rating(
        background_tasks: BackgroundTasks,
        book_id: UUID, 
        rating_id: UUID,
        rate_request: RateRequest,
        update_rating=Depends(update_rating_use_case), 
        user_id=Depends(get_current_user)):
    """
    Rate a book by its ID.
    """
    outcome: Outcome = update_rating.execute(rating_id=rating_id, book_id=book_id, user_id=user_id, love_score=rate_request.love_score, shit_score=rate_request.shit_score)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)

@router.post("/{book_id}/review")
async def review_book(
        background_tasks: BackgroundTasks,
        book_id: UUID, 
        review_request: ReviewRequest,
        review_book=Depends(create_review_use_case), 
        user_id=Depends(get_current_user)):
    """
    Review a book by its ID.
    """
    outcome: Outcome = review_book.execute(book_id=book_id, user_id=user_id, text=review_request.text, love_score=review_request.love_score, shit_score=review_request.shit_score)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)

    return {"message": "Book reviewed successfully"}

@router.post("/{book_id}/review/{review_id}/update")
async def update_review(
        background_tasks: BackgroundTasks,
        review_id: UUID,
        book_id: UUID, 
        review_request: ReviewRequest,
        update_review=Depends(update_review_use_case), 
        user_id=Depends(get_current_user)):
    """
    Review a book by its ID.
    """
    outcome: Outcome = update_review.execute(
        review_id=review_id,
        book_id=book_id, 
        user_id=user_id, 
        text=review_request.text, 
        love_score=review_request.love_score, 
        shit_score=review_request.shit_score)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)

    return {"message": "Book reviewed successfully"}

@router.get("/{book_id}/reviews")
async def get_book_reviews(
    book_id: UUID, 
    sort: str = "newest", 
    get_book_reviews=Depends(get_book_reviews_use_case)):
    """
    Get reviews of a book by its ID.
    """
    reviews = get_book_reviews.execute(book_id=book_id, sort=sort)
    return reviews

@router.get("/{book_id}/review")
async def get_review_or_rating(
    book_id: UUID,
    get_review=Depends(get_review_use_case),
    user_id=Depends(get_current_user)):
    outcome: Outcome = get_review.execute(book_id, user_id)

    print(outcome)

    if not outcome.isSuccess:
        raise HTTPException(status_code=outcome.failure.code, detail=outcome.failure.error)

    return outcome.data