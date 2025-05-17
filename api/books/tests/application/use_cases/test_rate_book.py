import pytest
from unittest.mock import MagicMock
from uuid import uuid4
from api.books.application.use_cases.rate_book import RateBook
from api.books.domain.models import Rating, Book, Author, RatingScore

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
        average_rating=0.0,
        number_of_ratings=0,
        sum_of_ratings=0.0
    )

@pytest.fixture
def mock_book_repository(mock_book):
    repo = MagicMock()
    repo.get_book_by_id = MagicMock(return_value=mock_book)
    repo.update_book = MagicMock()
    return repo

@pytest.fixture
def mock_rating_repository():
    repo = MagicMock()
    repo.get_rating_by_user_and_book = MagicMock(return_value=None)
    repo.create_rating = MagicMock()
    repo.update_rating = MagicMock()
    return repo

def test_rate_book_creates_new_rating(
    mock_book_repository, mock_rating_repository, book_id, user_id, mock_book
):
    # Arrange
    use_case = RateBook(mock_book_repository, mock_rating_repository)
    mock_rating_repository.get_rating_by_user_and_book.return_value = None

    # Act
    book = use_case.execute(book_id, user_id, 4.5)

    # Assert
    mock_book_repository.get_book_by_id.assert_called_once_with(book_id)
    mock_rating_repository.get_rating_by_user_and_book.assert_called_once_with(user_id, book_id)
    mock_rating_repository.create_rating.assert_called_once()
    mock_rating_repository.update_rating.assert_not_called()
    assert book.average_rating == 4.5
    assert book.number_of_ratings == 1
    assert book.sum_of_ratings == 4.5

def test_rate_book_raises_if_book_already_rated(
    mock_book_repository, mock_rating_repository, book_id, user_id, mock_book
):
    # Arrange
    use_case = RateBook(mock_book_repository, mock_rating_repository)
    initial_rating = Rating(uuid4(), book_id, user_id, RatingScore(4.0))
    
    # Setup mock for second rating
    mock_rating_repository.get_rating_by_user_and_book.return_value = initial_rating

    # Assert
    with pytest.raises(ValueError, match="Book already rated by user"):
        use_case.execute(book_id, user_id, 3.0)

def test_rate_book_raises_if_book_not_found(mock_rating_repository, book_id, user_id):
    # Arrange
    mock_book_repository = MagicMock()
    mock_book_repository.get_book_by_id.return_value = None
    use_case = RateBook(mock_book_repository, mock_rating_repository)

    # Act & Assert
    with pytest.raises(ValueError, match="Book not found"):
        use_case.execute(book_id, user_id, 5.0)