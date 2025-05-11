import pytest
from uuid import uuid4
from ratings.domain.models import Rating, Book

def test_rating_initialization():
    rating_id = uuid4()
    book_id = uuid4()
    user_id = uuid4()
    rating_value = 4.5

    rating = Rating(id=rating_id, book_id=book_id, user_id=user_id, rating=rating_value)

    assert rating.id == rating_id
    assert rating.book_id == book_id
    assert rating.user_id == user_id
    assert rating.rating == rating_value

def test_book_initialization():
    book_id = uuid4()
    title = "Test Book"
    author = "Test Author"

    book = Book(id=book_id, title=title, author=author)

    assert book.id == book_id
    assert book.title == title
    assert book.author == author
    assert book.ratings == []

def test_book_rate_add_new_rating():
    book_id = uuid4()
    user_id = uuid4()
    book = Book(id=book_id, title="Test Book", author="Test Author")

    rating_id = uuid4()
    rating_value = 4.0
    rating = Rating(id=rating_id, book_id=book_id, user_id=user_id, rating=rating_value)

    book.rate(user_id=user_id, rating=rating)

    assert len(book.ratings) == 1
    assert book.ratings[0].user_id == user_id
    assert book.ratings[0].rating == rating_value

def test_book_rate_update_existing_rating():
    book_id = uuid4()
    user_id = uuid4()
    book = Book(id=book_id, title="Test Book", author="Test Author")

    # Add initial rating
    rating_id = uuid4()
    initial_rating_value = 3.0
    initial_rating = Rating(id=rating_id, book_id=book_id, user_id=user_id, rating=initial_rating_value)
    book.rate(user_id=user_id, rating=initial_rating)

    # Update rating
    updated_rating_value = 4.5
    updated_rating = Rating(id=rating_id, book_id=book_id, user_id=user_id, rating=updated_rating_value)
    book.rate(user_id=user_id, rating=updated_rating)

    assert len(book.ratings) == 1
    assert book.ratings[0].user_id == user_id
    assert book.ratings[0].rating == updated_rating_value

def test_book_get_average_rating_no_ratings():
    book = Book(id=uuid4(), title="Test Book", author="Test Author")
    assert book.get_average_rating() == 0.0

def test_book_get_average_rating_with_ratings():
    book = Book(id=uuid4(), title="Test Book", author="Test Author")
    book.ratings = [
        Rating(id=uuid4(), book_id=book.id, user_id=uuid4(), rating=4.0),
        Rating(id=uuid4(), book_id=book.id, user_id=uuid4(), rating=5.0),
        Rating(id=uuid4(), book_id=book.id, user_id=uuid4(), rating=3.0),
    ]
    assert book.get_average_rating() == pytest.approx(4.0, rel=1e-2)