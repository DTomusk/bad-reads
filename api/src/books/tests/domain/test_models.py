from datetime import datetime, timezone
import pytest
from uuid import uuid4
from src.books.domain.models import ISBN13, Rating, Book, Author, RatingScore, Review

def test_rating_score_initialization():
    score = RatingScore(4.5)
    assert score.value == 4.5

def test_review_initialization():
    review_id = uuid4()
    rating_id = uuid4()
    text = "This is a test review"
    date_created = datetime.now(timezone.utc)
    book_id = uuid4()
    user_id = uuid4()

    review = Review(id=review_id, book_id=book_id, user_id=user_id, text=text, rating_id=rating_id, date_created=date_created)

    assert review.id == review_id
    assert review.text == text
    assert review.rating_id == rating_id
    assert review.date_created == date_created
    assert review.book_id == book_id
    assert review.user_id == user_id

def test_rating_score_validation():
    with pytest.raises(ValueError):
        RatingScore(-1)
    with pytest.raises(ValueError):
        RatingScore(5.5)

def test_rating_initialization():
    rating_id = uuid4()
    book_id = uuid4()
    user_id = uuid4()
    love_score = RatingScore(4.5)
    shit_score = RatingScore(1.0)

    rating = Rating(id=rating_id, book_id=book_id, user_id=user_id, love_score=love_score, shit_score=shit_score)

    assert rating.id == rating_id
    assert rating.book_id == book_id
    assert rating.user_id == user_id
    assert rating.love_score == love_score
    assert rating.shit_score == shit_score

def test_isbn13_initialization():
    isbn = ISBN13("9783161484100")
    assert isbn.value == "9783161484100"

def test_isbn13_standardization():
    isbn = ISBN13("978-3-16-148410-0")
    assert isbn.value == "9783161484100"

def test_isbn13_checksum():
    with pytest.raises(ValueError):
        ISBN13("978-3-16-148410-1")

def test_book_initialization():
    book_id = uuid4()
    title = "Test Book"
    author1 = Author(id=uuid4(), name="Test Author 1")
    author2 = Author(id=uuid4(), name="Test Author 2")
    authors = [author1, author2]
    isbn = ISBN13("978-3-16-148410-0")

    book = Book(
        id=book_id,
        title=title,
        authors=authors,
        average_love_rating=0.0,
        average_shit_rating=0.0,
        number_of_ratings=0,
        sum_of_love_ratings=0.0,
        sum_of_shit_ratings=0.0,
        isbn=isbn
    )

    assert book.id == book_id
    assert book.title == title
    assert book.authors == authors
    assert book.average_love_rating == 0.0
    assert book.average_shit_rating == 0.0
    assert book.number_of_ratings == 0
    assert book.sum_of_love_ratings == 0.0
    assert book.sum_of_shit_ratings == 0.0
    assert book.isbn == isbn

def test_book_add_rating():
    book_id = uuid4()
    user_id = uuid4()
    book = Book(
        id=book_id,
        title="Test Book",
        authors=[Author(id=uuid4(), name="Test Author")],
        average_love_rating=0.0,
        average_shit_rating=0.0,
        number_of_ratings=0,
        sum_of_love_ratings=0.0,
        sum_of_shit_ratings=0.0,
        isbn=ISBN13("978-3-16-148410-0")
    )

    rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=user_id,
        love_score=RatingScore(4.0),
        shit_score=RatingScore(1.0)
    )

    book.add_rating(rating)

    assert book.number_of_ratings == 1
    assert book.sum_of_love_ratings == 4.0
    assert book.average_love_rating == 4.0

def test_book_update_rating():
    book_id = uuid4()
    user_id = uuid4()
    book = Book(
        id=book_id,
        title="Test Book",
        authors=[Author(id=uuid4(), name="Test Author")],
        average_love_rating=0.0,
        average_shit_rating=0.0,
        number_of_ratings=0,
        sum_of_love_ratings=0.0,
        sum_of_shit_ratings=0.0,
        isbn=ISBN13("978-3-16-148410-0")
    )

    # Add initial rating
    initial_rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=user_id,
        love_score=RatingScore(3.0),
        shit_score=RatingScore(1.0)
    )
    book.add_rating(initial_rating)

    # Update rating
    updated_rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=user_id,
        love_score=RatingScore(4.5),
        shit_score=RatingScore(2.0)
    )
    
    book.update_rating(initial_rating, updated_rating)

    assert book.number_of_ratings == 1
    assert book.sum_of_love_ratings == 4.5
    assert book.average_love_rating == 4.5

def test_book_remove_rating():
    book_id = uuid4()
    book = Book(
        id=book_id,
        title="Test Book",
        authors=[Author(id=uuid4(), name="Test Author")],
        average_love_rating=4.0,
        average_shit_rating=2.0,
        number_of_ratings=1,
        sum_of_love_ratings=4.0,
        sum_of_shit_ratings=2.0,
        isbn=ISBN13("978-3-16-148410-0")
    )

    rating = Rating(
        id=uuid4(),
        book_id=book_id,
        user_id=uuid4(),
        love_score=RatingScore(4.0),
        shit_score=RatingScore(2.0)
    )

    book.remove_rating(rating)

    assert book.number_of_ratings == 0
    assert book.sum_of_love_ratings == 0
    assert book.average_love_rating == 0
    assert book.sum_of_shit_ratings == 0
    assert book.average_shit_rating == 0