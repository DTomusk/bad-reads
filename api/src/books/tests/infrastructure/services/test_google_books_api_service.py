import pytest
import httpx
from unittest.mock import MagicMock, patch, Mock
from src.books.infrastructure.services.google_books_api_service import GoogleBooksApiService
from src.books.domain.models import Book, Author


@pytest.fixture
def mock_google_books_response():
    return {
        "items": [
            {
                "volumeInfo": {
                    "title": "Test Book",
                    "authors": ["Test Author"],
                    "description": "Test Description",
                    "language": "en"
                }
            },
            {
                "volumeInfo": {
                    "title": "Another Book",
                    "authors": ["Author 1", "Author 2"],
                    "description": "Another Description",
                    "language": "en"
                }
            }
        ]
    }

@pytest.fixture
def mock_google_books_response_no_authors():
    return {
        "items": [
            {
                "volumeInfo": {
                    "title": "Test Book",
                    "authors": [],
                    "description": "Test Description",
                    "language": "en"
                }
            }
        ]
    }

@pytest.fixture
def mock_google_books_response_non_english():
    return {
        "items": [
            {
                "volumeInfo": {
                    "title": "Test Book",
                    "authors": ["Test Author"],
                    "description": "Test Description",
                    "language": "fr"
                }
            }
        ]
    }

@pytest.fixture
def mock_author_repository():
    repo = MagicMock()
    repo.get_author_by_name = MagicMock(return_value=None)
    repo.add_author = MagicMock(side_effect=lambda author: author)
    return repo

@pytest.fixture
def service(mock_author_repository):
    return GoogleBooksApiService(mock_author_repository)


def test_search_books_success(service, mock_google_books_response):
    with patch('httpx.get') as mock_get:
        # Configure the mock response
        mock_response = Mock()
        mock_response.json.return_value = mock_google_books_response
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Call the service
        books = service.search_books("test query")

        # Verify the results
        assert len(books) == 2
        assert all(isinstance(book, Book) for book in books)

        # Verify first book
        first_book = books[0]
        assert first_book.title == "Test Book"
        assert len(first_book.authors) == 1
        assert isinstance(first_book.authors[0], Author)
        assert first_book.authors[0].name == "Test Author"
        assert first_book.description == "Test Description"
        assert first_book.average_love_rating == 0.0
        assert first_book.average_shit_rating == 0.0
        assert first_book.number_of_ratings == 0
        assert first_book.sum_of_love_ratings == 0.0
        assert first_book.sum_of_shit_ratings == 0.0

        # Verify second book
        second_book = books[1]
        assert second_book.title == "Another Book"
        assert len(second_book.authors) == 2
        assert all(isinstance(author, Author) for author in second_book.authors)
        assert {author.name for author in second_book.authors} == {"Author 1", "Author 2"}
        assert second_book.description == "Another Description"
        assert second_book.average_love_rating == 0.0
        assert second_book.average_shit_rating == 0.0
        assert second_book.number_of_ratings == 0
        assert second_book.sum_of_love_ratings == 0.0
        assert second_book.sum_of_shit_ratings == 0.0

def test_search_books_no_authors(service, mock_google_books_response_no_authors):
    with patch('httpx.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = mock_google_books_response_no_authors
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        books = service.search_books("test query")
        assert len(books) == 0


def test_search_books_no_results(service):
    with patch('httpx.get') as mock_get:
        # Configure the mock response with no items
        mock_response = Mock()
        mock_response.json.return_value = {"items": []}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Call the service
        books = service.search_books("test query")

        # Verify empty results
        assert len(books) == 0


def test_search_books_http_error(service):
    with patch('httpx.get') as mock_get:
        # Configure the mock to raise an HTTP error
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = httpx.HTTPError("Test error")
        mock_get.return_value = mock_response

        # Verify that the error is propagated
        with pytest.raises(httpx.HTTPError):
            service.search_books("test query")

def test_search_books_non_english(service, mock_google_books_response_non_english):
    with patch('httpx.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = mock_google_books_response_non_english
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        books = service.search_books("test query")
        assert len(books) == 0

