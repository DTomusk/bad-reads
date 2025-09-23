from unittest.mock import MagicMock
from uuid import uuid4
import pytest

from src.books.application.services.rating_with_review_service import RatingWithReviewService
from src.books.domain.models import Rating, Review


@pytest.fixture
def rating_ids():
    return [uuid4(), uuid4(), uuid4()]

@pytest.fixture
def book_ids():
    return [uuid4(), uuid4(), uuid4()]

@pytest.fixture
def user_id():
    return uuid4()

@pytest.fixture
def review_ids():
    return [uuid4(), uuid4(), uuid4()]

@pytest.fixture
def mock_ratings(rating_ids, book_ids, user_id):
    return [
        Rating(id=rating_ids[1], book_id=book_ids[1], user_id=user_id, love_score=1, shit_score=3),
        Rating(id=rating_ids[2], book_id=book_ids[2], user_id=user_id, love_score=2, shit_score=4),
        Rating(id=rating_ids[0], book_id=book_ids[0], user_id=user_id, love_score=4.5, shit_score=2)
    ]

@pytest.fixture
def mock_reviews(review_ids, rating_ids, book_ids, user_id):
    return [
        Review(id=review_ids[0], rating_id=rating_ids[0], book_id=book_ids[0], user_id=user_id, text="blah"),
        Review(id=review_ids[1], rating_id=rating_ids[1], book_id=book_ids[1], user_id=user_id, text="foo"),
        Review(id=review_ids[2], rating_id=rating_ids[2], book_id=book_ids[2], user_id=user_id, text="bar")
    ]

@pytest.fixture
def mock_rating_repo(mock_ratings):
    repo = MagicMock()
    repo.get_ratings_for_ids = MagicMock(return_value=mock_ratings)
    return repo

def test_get_ratings_with_reviews_from_reviews_no_reviews(mock_rating_repo):
    # Arrange
    service = RatingWithReviewService(rating_repo=mock_rating_repo)
    mock_rating_repo.get_ratings_for_ids.return_value = []

    # Act
    result = service.get_ratings_with_reviews_from_reviews([])

    # Assert
    mock_rating_repo.get_ratings_for_ids.assert_called_once_with([])
    assert len(result) == 0

def test_get_ratings_with_reviews_from_reviews(mock_rating_repo, mock_reviews):
    # Arrange
    service = RatingWithReviewService(rating_repo=mock_rating_repo)

    # Act
    result = service.get_ratings_with_reviews_from_reviews(mock_reviews)

    # Assert
    mock_rating_repo.get_ratings_for_ids.assert_called_once_with([review.rating_id for review in mock_reviews])
    assert len(result) == len(mock_reviews)
    # Order should be the same as the reviews'
    assert result[0].review_id == mock_reviews[0].id
    assert result[1].review_id == mock_reviews[1].id
    assert result[2].review_id == mock_reviews[2].id