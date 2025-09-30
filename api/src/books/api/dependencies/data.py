from fastapi import Depends

from ...data.rating_with_review_reader import RatingWithReviewReader
from ...data.author_repository import AuthorRepo
from ...data.book_repository import BookRepo
from ...data.rating_repository import RatingRepo
from ...data.review_repository import ReviewRepo
from ....infrastructure.db.database import get_session


def get_ratings_repo(session=Depends(get_session)):
    """
    Dependency to provide the Ratings repository.
    """
    return RatingRepo(session=session)

def get_rating_with_review_reader(session=Depends(get_session)):
    """
    Dependency to provide the Rating with Review reader.
    """
    return RatingWithReviewReader(session=session)

def get_reviews_repo(session=Depends(get_session)):
    """
    Dependency to provide the Reviews repository.
    """
    return ReviewRepo(session=session)

def get_books_repo(session=Depends(get_session)):
    """
    Dependency to provide the Books repository.
    """
    return BookRepo(session=session)

def get_authors_repo(session=Depends(get_session)):
    """
    Dependency to provide the Authors repository.
    """
    return AuthorRepo(session=session)