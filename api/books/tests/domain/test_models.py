from datetime import datetime, timezone
import pytest
from uuid import uuid4
from api.books.domain.models import Rating, Book, Author, RatingScore, Review

def test_rating_score_initialization():
    score = RatingScore(4.5)
    assert score.value == 4.5

def test_review_initialization():
    review_id = uuid4()
    rating_id = uuid4()
    text = "This is a test review"
    date_created = datetime.now(timezone.utc)

    review = Review(id=review_id, text=text, rating_id=rating_id, date_created=date_created)

    assert review.id == review_id
    assert review.text == text
    assert review.rating_id == rating_id
    assert review.date_created == date_created

def test_rating_score_validation():
    with pytest.raises(ValueError):
        RatingScore(-1)
    with pytest.raises(ValueError):
        RatingScore(5.5)

def test_rating_initialization():
    rating_id = uuid4()
    book_id = uuid4()
    user_id = uuid4()
    score = RatingScore(4.5)

    rating = Rating(id=rating_id, book_id=book_id, user_id=user_id, score=score)

    assert rating.id == rating_id
    assert rating.book_id == book_id
    assert rating.user_id == user_id
    assert rating.score == score

def test_book_initialization():
    book_id = uuid4()
    title = "Test Book"
    author1 = Author(id=uuid4(), name="Test Author 1")
    author2 = Author(id=uuid4(), name="Test Author 2")
    authors = [author1, author2]

    book = Book(
        id=book_id,
        title=title,
        authors=authors,
        average_rating=0.0,
        number_of_ratings=0,
        sum_of_ratings=0.0
    )

    assert book.id == book_id
    assert book.title == title
    assert book.authors == authors
    assert book.average_rating == 0.0
    assert book.number_of_ratings == 0
    assert book.sum_of_ratings == 0.0

def test_book_add_rating():
    book_id = uuid4()
    user_id = uuid4()
    book = Book(
        id=book_id,
        title="Test Book",
        authors=[Author(id=uuid4(), name="Test Author")],
        average_rating=0.0,
        number_of_ratings=0,
        sum_of_ratings=0.0
    )

    rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=user_id,
        score=RatingScore(4.0)
    )

    book.add_rating(rating)

    assert book.number_of_ratings == 1
    assert book.sum_of_ratings == 4.0
    assert book.average_rating == 4.0

def test_book_update_rating():
    book_id = uuid4()
    user_id = uuid4()
    book = Book(
        id=book_id,
        title="Test Book",
        authors=[Author(id=uuid4(), name="Test Author")],
        average_rating=0.0,
        number_of_ratings=0,
        sum_of_ratings=0.0
    )

    # Add initial rating
    initial_rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=user_id,
        score=RatingScore(3.0)
    )
    book.add_rating(initial_rating)

    # Update rating
    updated_rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=user_id,
        score=RatingScore(4.5)
    )
    
    book.update_rating(initial_rating, updated_rating)

    assert book.number_of_ratings == 1
    assert book.sum_of_ratings == 4.5
    assert book.average_rating == 4.5

def test_book_remove_rating():
    book_id = uuid4()
    book = Book(
        id=book_id,
        title="Test Book",
        authors=[Author(id=uuid4(), name="Test Author")],
        average_rating=4.0,
        number_of_ratings=1,
        sum_of_ratings=4.0
    )

    rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=uuid4(),
        score=RatingScore(4.0)
    )

    book.remove_rating(rating)

    assert book.number_of_ratings == 0
    assert book.sum_of_ratings == 0
    assert book.average_rating == 0