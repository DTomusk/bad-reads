from fastapi import Depends

from ...users.api.dependencies import get_user_repository
from ...books.api.dependencies.data import get_rating_with_review_reader
from ..application.queries.get_reviews_with_username_for_book import GetReviewsWithUsernamesForBook


def get_reviews_with_username_query(
        rating_with_review_reader=Depends(get_rating_with_review_reader),
        user_repo=Depends(get_user_repository)):
    return GetReviewsWithUsernamesForBook(
        rating_with_review_reader=rating_with_review_reader, 
        user_repo=user_repo)