import pytest
from unittest.mock import MagicMock
from uuid import uuid4
from src.books.application.use_cases.get_book_details import GetBookDetails
from src.books.domain.models import Author

@pytest.fixture
def book_id():
    return uuid4()

@pytest.fixture
def mock_book():
    mock = MagicMock()
    mock.id = uuid4()
    mock.title = "Test Book"
    mock.authors = [Author(id=uuid4(), name="Test Author")]
    mock.average_love_rating = 4.5
    mock.average_shit_rating = 2.0
    mock.number_of_ratings = 10
    mock.sum_of_love_ratings = 45.0
    mock.sum_of_shit_ratings = 20.0
    mock.picture_url = "https://example.com/picture.jpg"
    mock.description = "Test Description"
    return mock

@pytest.fixture
def mock_book_repository(mock_book):
    repo = MagicMock()
    repo.get_book_by_id = MagicMock(return_value=mock_book)
    return repo

@pytest.fixture
def mock_rating_repository():
    repo = MagicMock()
    return repo

def test_get_book_details_returns_book(mock_book_repository, mock_rating_repository, book_id, mock_book):
    # Arrange
    use_case = GetBookDetails(mock_book_repository, mock_rating_repository)

    # Act
    result = use_case.execute(book_id)

    # Assert
    mock_book_repository.get_book_by_id.assert_called_once_with(book_id)
    assert result is not None
    assert result.title == mock_book.title
    assert result.authors == [author.name for author in mock_book.authors]
    assert result.average_love_rating == mock_book.average_love_rating
    assert result.average_shit_rating == mock_book.average_shit_rating
    assert result.number_of_ratings == mock_book.number_of_ratings
    assert result.sum_of_love_ratings == mock_book.sum_of_love_ratings
    assert result.sum_of_shit_ratings == mock_book.sum_of_shit_ratings

def test_get_book_details_raises_if_book_not_found(mock_rating_repository, book_id):
    # Arrange
    mock_book_repository = MagicMock()
    mock_book_repository.get_book_by_id.return_value = None
    use_case = GetBookDetails(mock_book_repository, mock_rating_repository)

    # Act & Assert
    with pytest.raises(ValueError, match="Book not found"):
        use_case.execute(book_id)