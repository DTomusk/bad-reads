# Just to create some data to play around with
# to be removed at a later stage

from sqlalchemy.orm import Session
from api.infrastructure.db.database import Base, engine, SessionLocal
from api.books.infrastructure.models import AuthorModel, BookModel
import uuid

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
                    average_rating=0.0,
                    number_of_ratings=0,
                    sum_of_ratings=0.0,
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

if __name__ == "__main__":
    seed_books()