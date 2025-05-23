import pytest
from unittest.mock import MagicMock
from uuid import uuid4
from src.books.application.use_cases.get_book_details import GetBookDetails

@pytest.fixture
def book_id():
    return uuid4()

@pytest.fixture
def mock_book():
    mock = MagicMock()
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
    assert result['book'] is not None
    assert result['ratings'] is not None
    assert result['book'].id == mock_book.id
    assert result['book'].title == mock_book.title
    assert result['book'].authors == mock_book.authors
    assert result['book'].average_rating == mock_book.average_rating
    assert result['book'].number_of_ratings == mock_book.number_of_ratings
    assert result['book'].sum_of_ratings == mock_book.sum_of_ratings

def test_get_book_details_raises_if_book_not_found(mock_rating_repository, book_id):
    # Arrange
    mock_book_repository = MagicMock()
    mock_book_repository.get_book_by_id.return_value = None
    use_case = GetBookDetails(mock_book_repository, mock_rating_repository)

    # Act & Assert
    with pytest.raises(ValueError, match="Book not found"):
        use_case.execute(book_id)