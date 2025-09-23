from abc import ABC

from src.books.application.repositories.rating_repository import AbstractRatingRepo
from src.books.domain.models import RatingWithReview, RatingWithReviewFactory, Review


class AbstractRatingWithReviewService(ABC):
    def get_ratings_with_reviews_from_reviews(reviews: list[Review]) -> list[RatingWithReview]:
        """ For a list of reviews, get ratings with reviews in the same order as the reviews"""
        pass

class RatingWithReviewService(AbstractRatingWithReviewService):
    def __init__(self, rating_repo: AbstractRatingRepo):
        self.rating_repo = rating_repo

    def get_ratings_with_reviews_from_reviews(self, reviews: list[Review]):
        print("Reviews: ", reviews)
        rating_ids = [review.rating_id for review in reviews]
        print("Rating ids: ", rating_ids)
        ratings = self.rating_repo.get_ratings_for_ids(rating_ids)
        print("Ratings: ", ratings)

        return RatingWithReviewFactory.create_list(ratings=ratings, reviews=reviews)
