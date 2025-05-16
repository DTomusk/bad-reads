from api.books.application.use_cases.get_book_details import GetBookDetails
from api.books.infrastructure.repositories.sqlite_book_repo import SqliteBookRepo
from api.books.infrastructure.repositories.sqlite_rating_repo import SqliteRatingRepo
from api.books.tests.integration.conftest import book_repo, rating_repo, book1, book2, book3

def test_get_book_details_integration(book_repo, rating_repo):
    # Arrange
    use_case = GetBookDetails(book_repo, rating_repo)

    # Act
    result = use_case.execute(book_id=book1.id)

    # Assert
    assert result.id == book1.id
    assert result.title == book1.title