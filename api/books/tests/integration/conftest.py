from uuid import UUID
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.infrastructure.db.database import Base
from api.books.infrastructure.models import AuthorModel, BookModel
from api.books.infrastructure.repositories.sqlite_book_repo import SqliteBookRepo
from api.books.infrastructure.repositories.sqlite_rating_repo import SqliteRatingRepo

TEST_DB_URL = "sqlite:///./test.db"  # DB for testing purposes

engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

author1 = AuthorModel(id=UUID("1fefb0a4-1c2e-4f3b-8d5e-1f7a0c6b8d9f"), name="George Orwell")
author2 = AuthorModel(id=UUID("2fefb0a4-1c2e-4f3b-8d5e-1f7a0c6b8d9f"), name="Aldous Huxley")
author3 = AuthorModel(id=UUID("3fefb0a4-1c2e-4f3b-8d5e-1f7a0c6b8d9f"), name="Ray Bradbury")

book1 = BookModel(id=UUID("1eefb0a4-1c2e-4f3b-8d5e-1f7a0c6b8d9f"), title="1984", authors=[author1], average_rating=0, number_of_ratings=0, sum_of_ratings=0)
book2 = BookModel(id=UUID("2eefb0a4-1c2e-4f3b-8d5e-1f7a0c6b8d9f"), title="Brave New World", authors=[author2], average_rating=0, number_of_ratings=0, sum_of_ratings=0)
book3 = BookModel(id=UUID("3eefb0a4-1c2e-4f3b-8d5e-1f7a0c6b8d9f"), title="Fahrenheit 451", authors=[author3], average_rating=0, number_of_ratings=0, sum_of_ratings=0)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    # seed data
    session.add_all([book1, book2, book3])
    session.commit()

    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def book_repo(db_session):
    return SqliteBookRepo(session=db_session)

@pytest.fixture
def rating_repo(db_session):
    return SqliteRatingRepo(session=db_session)