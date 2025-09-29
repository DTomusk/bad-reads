import pytest
from unittest.mock import MagicMock
from uuid import uuid4
from src.infrastructure.api.models import Outcome
from src.books.application.use_cases.commands.create_rating import CreateRating
from src.books.domain.models import Book, Author

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
    )

@pytest.fixture
def mock_rating_service():
    repo = MagicMock()
    return repo

@pytest.fixture
def mock_rating_repository():
    repo = MagicMock()
    repo.get_rating_by_user_and_book = MagicMock(return_value=None)
    repo.create_rating = MagicMock()
    repo.update_rating = MagicMock()
    return repo

@pytest.fixture
def mock_review_repo():
    repo = MagicMock()
    return repo

def test_rate_book_creates_new_rating_without_review(
    mock_rating_service, mock_rating_repository, mock_review_repo, book_id, user_id, mock_book
):
    # Arrange
    use_case = CreateRating(mock_rating_service, mock_rating_repository, mock_review_repo)
    mock_rating_repository.get_rating_by_user_and_book.return_value = None
    mock_rating_service.create_rating.return_value = Outcome(isSuccess=True)

    # Act
    outcome = use_case.execute(book_id, user_id, 4.5, 2.0)

    # Assert
    mock_rating_repository.get_rating_by_user_and_book.assert_called_once_with(user_id=user_id, book_id=book_id)
    mock_rating_service.create_rating.assert_called_once_with(book_id=book_id, user_id=user_id, love_score=4.5, shit_score=2.0)
    mock_rating_service.update_rating.assert_not_called()
    mock_review_repo.create_review.assert_not_called()
    assert outcome is not None
    assert outcome.isSuccess is True

    # TODO: add more tests for new ratings with reviews and updated ratings with different review states

# def test_rate_book_raises_if_book_already_rated(
#     mock_book_repository, mock_rating_repository, book_id, user_id, mock_book
# ):
#     # Arrange
#     use_case = CreateRating(mock_book_repository, mock_rating_repository)
#     initial_rating = Rating(uuid4(), book_id, user_id, RatingScore(4.0), RatingScore(2.0))
    
#     # Setup mock for second rating
#     mock_rating_repository.get_rating_by_user_and_book.return_value = initial_rating

#     # Assert
#     with pytest.raises(ValueError, match="Book already rated by user"):
#         use_case.execute(book_id, user_id, 3.0, 1.0)

# def test_rate_book_raises_if_book_not_found(mock_rating_repository, book_id, user_id):
#     # Arrange
#     mock_book_repository = MagicMock()
#     mock_book_repository.get_book_by_id.return_value = None
#     use_case = CreateRating(mock_book_repository, mock_rating_repository)

#     # Act & Assert
#     with pytest.raises(ValueError, match="Book not found"):
#         use_case.execute(book_id, user_id, 5.0, 3.0)