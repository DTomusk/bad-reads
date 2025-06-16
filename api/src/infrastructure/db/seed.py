# Just to create some data to play around with
# to be removed at a later stage

import random
from sqlalchemy.orm import Session
from src.infrastructure.db.database import Base, engine, SessionLocal
from src.books.infrastructure.models import AuthorModel, BookModel
import uuid

from src.users.infrastructure.models import UserModel

BOOKS = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Moby-Dick", "author": "Herman Melville"},
    {"title": "War and Peace", "author": "Leo Tolstoy"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "Brave New World", "author": "Aldous Huxley"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"title": "The Odyssey", "author": "Homer"},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë"},
    {"title": "Wuthering Heights", "author": "Emily Brontë"},
    {"title": "Great Expectations", "author": "Charles Dickens"},
    {"title": "The Divine Comedy", "author": "Dante Alighieri"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy"},
    {"title": "Don Quixote", "author": "Miguel de Cervantes"},
    {"title": "Ulysses", "author": "James Joyce"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
    {"title": "The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle"},
    {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas"},
    {"title": "The Old Man and the Sea", "author": "Ernest Hemingway"},
    {"title": "The Scarlet Letter", "author": "Nathaniel Hawthorne"},
]

# Note: You can't log in as these users because these aren't valid hashed passwords
USERS = [
    {"email": "test@test.com", "password": "test"},
    {"email": "test2@test.com", "password": "test"},
    {"email": "test3@test.com", "password": "test"},
    {"email": "test4@test.com", "password": "test"},
    {"email": "test5@test.com", "password": "test"},
]

Base.metadata.create_all(bind=engine)

def seed_books():
    session: Session = SessionLocal()
    book_counter = 0
    author_counter = 0
    try:
        # First pass: Create all authors
        authors_map = {}  # Keep track of authors we've already created
        for book in BOOKS:
            author_name = book["author"]
            if author_name not in authors_map:
                author_obj = session.query(AuthorModel).filter(AuthorModel.name == author_name).first()
                if not author_obj:
                    author_obj = AuthorModel(
                        id=uuid.uuid4(),
                        name=author_name
                    )
                    session.add(author_obj)
                    author_counter += 1
                authors_map[author_name] = author_obj
        
        # Commit authors first
        session.commit()

        # Second pass: Create all books
        for book in BOOKS:
            book_obj = session.query(BookModel).filter(BookModel.title == book["title"]).first()
            if not book_obj:
                book_obj = BookModel(
                    id=uuid.uuid4(),
                    title=book["title"],
                    average_love_rating=0.0,
                    average_shit_rating=0.0,
                    number_of_ratings=0,
                    sum_of_love_ratings=0.0,
                    sum_of_shit_ratings=0.0,
                    authors=[authors_map[book["author"]]]
                )
                session.add(book_obj)
                book_counter += 1
        
        # Commit books
        session.commit()
        print(f"Seeded {book_counter} books and {author_counter} authors successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error seeding books: {e}")
    finally:
        session.close()

def seed_users():
    session: Session = SessionLocal()
    user_counter = 0
    try:
        for user in USERS:
            user_obj = session.query(UserModel).filter(UserModel.email == user["email"]).first()
            if not user_obj:
                user_obj = UserModel(
                    id=uuid.uuid4(),
                    email=user["email"],
                    hashed_password=user["password"]
                )
                session.add(user_obj)
                user_counter += 1
        session.commit()
        print(f"Seeded {user_counter} users successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error seeding users: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_books()
    seed_users()
