# Just to create some data to play around with
# to be removed at a later stage

from sqlalchemy.orm import Session
from api.infrastructure.db.database import Base, engine, SessionLocal
from api.ratings.infrastructure.models import BookModel
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
]

Base.metadata.create_all(bind=engine)

def seed_books():
    session: Session = SessionLocal()
    try:
        for book in BOOKS:
            book_obj = BookModel(
                id=uuid.uuid4(),
                title=book["title"],
                author=book["author"]
            )
            session.add(book_obj)
        session.commit()
        print("Seeded 20 books successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error seeding books: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_books()