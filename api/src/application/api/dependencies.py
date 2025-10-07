from fastapi import Depends

from ..data.review_with_username_reader import ReviewWithUsernameReader

from ...infrastructure.db.database import get_session

def get_reviews_with_username_reader(session=Depends(get_session)):
    return ReviewWithUsernameReader(session=session)
    return GetReviewsWithUsernamesForBook(
        review_with_username_reader=reviews_with_username_reader)