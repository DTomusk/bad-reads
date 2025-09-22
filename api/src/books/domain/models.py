from dataclasses import dataclass
from datetime import datetime, timezone
import re
from uuid import UUID

@dataclass(frozen=True)
class RatingScore:
    value: float

    def __post_init__(self):
        if self.value < 0 or self.value > 5:
            raise ValueError("Rating score must be between 0 and 5")

class Rating:
    """ Represents a rating given by a user to a book """
    def __init__(self, id: UUID, book_id: UUID, user_id: UUID, love_score: RatingScore, shit_score: RatingScore):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.love_score = love_score
        self.shit_score = shit_score

class Review:
    """ Represents a review given by a user to a book """
    def __init__(self, id: UUID, book_id: UUID, user_id: UUID, text: str, rating_id: UUID, date_created: datetime = datetime.now(timezone.utc)):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.text = text
        self.rating_id = rating_id
        self.date_created = date_created

class RatingWithReview: 
    """ Represents a Rating with a Review """
    def __init__(
        self, 
        rating_id: UUID, 
        review_id: UUID, 
        book_id: UUID, 
        user_id: UUID, 
        love_score: RatingScore, 
        shit_score: RatingScore, 
        text: str,
        date_created: datetime):
        self.rating_id = rating_id
        self.review_id = review_id
        self.book_id = book_id
        self.user_id = user_id
        self.love_score = love_score
        self.shit_score = shit_score
        self.text = text
        self.date_created = date_created

class RatingWithReviewFactory: 
    def create(rating: Rating, review: Review) -> RatingWithReview:
        if rating.id != review.rating_id:
            raise ValueError("Used wrong review for rating")
        if rating.book_id != review.book_id:
            raise ValueError("Rating and review refer to different books")
        if rating.user_id != review.user_id:
            raise ValueError("Rating and review were created by different users")
        return RatingWithReview(
            rating_id=rating.id, 
            review_id=review.id,
            book_id=rating.book_id,
            user_id=rating.user_id,
            love_score=rating.love_score,
            shit_score=rating.shit_score,
            text=review.text,
            date_created=review.date_created
            )
    
    def create_list(ratings: list[Rating], reviews: list[Review]) -> list[RatingWithReview]:
        combined: list[RatingWithReview] = []
        rating_map = {r.id: r for r in ratings}

        for review in reviews: 
            rating = rating_map.get(review.rating_id)
            if rating is None: 
                raise ValueError("Rating not found for review in list")
            rating_with_review: RatingWithReview = RatingWithReviewFactory.create(rating=rating, review=review)
            combined.append(rating_with_review)

        return combined

class Author:
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name

class Book:
    def __init__(
            self, 
            id: UUID, 
            title: str, 
            authors: list[Author], 
            average_love_rating: float, 
            average_shit_rating: float, 
            number_of_ratings: int,
            sum_of_love_ratings: float,
            sum_of_shit_ratings: float,
            description: str | None = None,
            picture_url: str | None = None,
            ):
        self.id = id
        self.title = title
        self.authors = authors
        self.average_love_rating = average_love_rating
        self.average_shit_rating = average_shit_rating
        self.number_of_ratings = number_of_ratings
        self.sum_of_love_ratings = sum_of_love_ratings
        self.sum_of_shit_ratings = sum_of_shit_ratings
        self.description = description
        self.picture_url = picture_url

    def add_rating(self, rating: Rating) -> None:
        """ Add a rating to the book """
        if self.sum_of_love_ratings is None:
            self.sum_of_love_ratings = 0
        if self.sum_of_shit_ratings is None:
            self.sum_of_shit_ratings = 0
        if self.number_of_ratings is None:
            self.number_of_ratings = 0
        if self.average_love_rating is None:
            self.average_love_rating = 0
        if self.average_shit_rating is None:
            self.average_shit_rating = 0
        self.sum_of_love_ratings += rating.love_score.value
        self.sum_of_shit_ratings += rating.shit_score.value
        self.number_of_ratings += 1
        self.average_love_rating = self.sum_of_love_ratings / self.number_of_ratings
        self.average_shit_rating = self.sum_of_shit_ratings / self.number_of_ratings

    def remove_rating(self, rating: Rating) -> None:
        """ Remove a rating from the book """
        self.sum_of_love_ratings -= rating.love_score.value
        self.sum_of_shit_ratings -= rating.shit_score.value
        self.number_of_ratings -= 1
        if self.number_of_ratings > 0:
            self.average_love_rating = self.sum_of_love_ratings / self.number_of_ratings
            self.average_shit_rating = self.sum_of_shit_ratings / self.number_of_ratings
        else:
            self.average_love_rating = 0
            self.average_shit_rating = 0

    def update_rating(self, old_rating: Rating, new_rating: Rating) -> None:
        """ Update a rating for the book """
        self.remove_rating(old_rating)
        self.add_rating(new_rating)
