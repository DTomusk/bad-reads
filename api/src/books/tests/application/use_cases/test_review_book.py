from datetime import datetime, timezone
from unittest.mock import MagicMock
from uuid import uuid4
import pytest

from src.books.application.use_cases.reviews.review_book import ReviewBook
from src.books.domain.models import Author, Book, Rating, RatingScore, Review

@pytest.fixture
def book_id():
    return uuid4()

@pytest.fixture
def user_id():
    return uuid4()

@pytest.fixture
def mock_book(book_id):
    return Book(
        id=book_id, 
        title="Test Book", 
        authors=[Author(id=uuid4(), name="Test Author")], 
        average_love_rating=0.0, 
        average_shit_rating=0.0, 
        number_of_ratings=0, 
        sum_of_love_ratings=0.0, 
        sum_of_shit_ratings=0.0, 
        description="Test Description"
    )

@pytest.fixture
def mock_book_repository(mock_book):
    repo = MagicMock()
    repo.get_book_by_id = MagicMock(return_value=mock_book)
    return repo

@pytest.fixture
def mock_rating_repository():
    repo = MagicMock()
    repo.get_rating_by_user_and_book = MagicMock(return_value=None)
    return repo

@pytest.fixture
def mock_review_repository():
    repo = MagicMock()
    repo.get_review_by_user_and_book = MagicMock(return_value=None)
    return repo

def test_review_book_creates_new_review(mock_book_repository, mock_rating_repository, mock_review_repository, book_id, user_id, mock_book):
    # Arrange
    use_case = ReviewBook(mock_book_repository, mock_rating_repository, mock_review_repository)

    # Act
    use_case.execute(book_id, user_id, "Test Review", 4.5, 2.0)

    # Assert
    mock_book_repository.get_book_by_id.assert_called_once_with(book_id)
    mock_rating_repository.get_rating_by_user_and_book.assert_called_once_with(user_id, book_id)
    mock_review_repository.create_review.assert_called_once()

def test_review_book_raises_if_book_not_found(mock_book_repository, mock_rating_repository, mock_review_repository, book_id, user_id, mock_book):
    # Arrange
    use_case = ReviewBook(mock_book_repository, mock_rating_repository, mock_review_repository)
    mock_book_repository.get_book_by_id.return_value = None

    # Act & Assert
    with pytest.raises(ValueError, match="Book not found"):
        use_case.execute(book_id, user_id, "Test Review", 4.5, 2.0)

    assert mock_book_repository.get_book_by_id.call_count == 1
    assert mock_rating_repository.get_rating_by_user_and_book.call_count == 0
    assert mock_review_repository.create_review.call_count == 0

def test_review_book_raises_if_book_already_rated(mock_book_repository, mock_rating_repository, mock_review_repository, book_id, user_id, mock_book):
    # Arrange
    use_case = ReviewBook(mock_book_repository, mock_rating_repository, mock_review_repository)
    mock_rating_repository.get_rating_by_user_and_book.return_value = Rating(id=uuid4(), book_id=book_id, user_id=user_id, love_score=RatingScore(4.5), shit_score=RatingScore(2.0))

    # Act & Assert
    with pytest.raises(ValueError, match="Book already rated by user"):
        use_case.execute(book_id, user_id, "Test Review", 4.5, 2.0)

    assert mock_book_repository.get_book_by_id.call_count == 1
    assert mock_rating_repository.get_rating_by_user_and_book.call_count == 1
    assert mock_review_repository.create_review.call_count == 0

def test_review_book_raises_if_book_already_reviewed(mock_book_repository, mock_rating_repository, mock_review_repository, book_id, user_id, mock_book):
    # Arrange
    use_case = ReviewBook(mock_book_repository, mock_rating_repository, mock_review_repository)
    mock_review_repository.get_review_by_user_and_book.return_value = Review(id=uuid4(), book_id=book_id, user_id=user_id, text="Test Review", rating_id=uuid4(), date_created=datetime.now(timezone.utc))

    # Act & Assert
    with pytest.raises(ValueError, match="Book already reviewed by user"):
        use_case.execute(book_id, user_id, "Test Review", 4.5, 2.0)

    assert mock_book_repository.get_book_by_id.call_count == 1
    assert mock_rating_repository.get_rating_by_user_and_book.call_count == 1
    assert mock_review_repository.create_review.call_count == 0
