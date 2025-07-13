from sqlalchemy import UUID, func
from sqlalchemy.orm import Session

from src.books.application.repositories.book_repository import AbstractBookRepo
from src.books.domain.models import Book
from src.books.infrastructure.models import BookModel, AuthorModel
from src.infrastructure.utilities.text_normalizer import normalize_text


class BookRepo(AbstractBookRepo):
    def __init__(self, session: Session):
        self.session = session

    def _create_book_from_db_result(self, result: BookModel) -> Book:
        """Create a Book domain model from a database result.
        
        Args:
            result: A BookModel instance from the database
            
        Returns:
            Book: A new Book domain model instance
        """
        return Book(
            id=result.id,
            title=result.title,
            authors=result.authors,
            average_love_rating=result.average_love_rating if result.average_love_rating else 0,
            average_shit_rating=result.average_shit_rating if result.average_shit_rating else 0,
            number_of_ratings=result.number_of_ratings if result.number_of_ratings else 0,
            sum_of_love_ratings=result.sum_of_love_ratings if result.sum_of_love_ratings else 0,
            sum_of_shit_ratings=result.sum_of_shit_ratings if result.sum_of_shit_ratings else 0,
            description=result.description,
            picture_url=result.picture_url
        )
    
    def _create_book_model_from_domain_model(self, book: Book) -> BookModel:
        """Create a BookModel instance from a Book domain model.
        
        Args:
            book: A Book domain model instance
            
        """
        # First get the author models for all authors
        author_models = []
        for author in book.authors:
            author_model = self.session.query(AuthorModel).filter(AuthorModel.id == author.id).first()
            if author_model:
                author_models.append(author_model)

        book_model = BookModel(
            id=book.id,
            title=book.title,
            normalized_title=normalize_text(book.title),
            average_love_rating=book.average_love_rating if book.average_love_rating else 0,
            average_shit_rating=book.average_shit_rating if book.average_shit_rating else 0,
            number_of_ratings=book.number_of_ratings if book.number_of_ratings else 0,
            sum_of_love_ratings=book.sum_of_love_ratings if book.sum_of_love_ratings else 0,
            sum_of_shit_ratings=book.sum_of_shit_ratings if book.sum_of_shit_ratings else 0,
            description=book.description,
            picture_url=book.picture_url,
            authors=author_models  # Set up the many-to-many relationship
        )
        return book_model
    
    def get_book_by_id(self, book_id: UUID) -> Book:
        """
        Get a book by its ID.
        :param book_id: The ID of the book to retrieve.
        :return: The book object.
        """
        result = self.session.query(BookModel).filter(BookModel.id == book_id).first()
        if result:
            return self._create_book_from_db_result(result)
    
    def get_books(self, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Book]:
        """
        Get all books.
        :return: A list of book objects.
        """
        result = (self.session.query(BookModel)
            .order_by(getattr(BookModel, sort_by).asc() if sort_order == "asc" else getattr(BookModel, sort_by).desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all())
        return [self._create_book_from_db_result(book) for book in result]
    
    def get_books_by_author(self, author_id: UUID, page: int = 1, page_size: int = 10, sort_by: str = "title", sort_order: str = "asc") -> list[Book]:
        """
        Get books by author.
        :param author_id: The ID of the author to filter by
        :param page: The page number for pagination
        :param page_size: The number of items per page
        :param sort_by: The field to sort by
        :param sort_order: The sort order ('asc' or 'desc')
        :return: A list of book objects.
        """
        result = (self.session.query(BookModel)
            .join(BookModel.authors)
            .filter(AuthorModel.id == author_id)
            .order_by(getattr(BookModel, sort_by).asc() if sort_order == "asc" else getattr(BookModel, sort_by).desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all())
        return [self._create_book_from_db_result(book) for book in result]
        
    def get_book_by_title_and_author(self, title: str, author_name: str) -> Book:
        """
        Get a book by its title and author.
        :param title: The title of the book to retrieve.
        :param author_name: The name of the author of the book to retrieve.
        :return: The book object.
        """
        # TODO: use fuzzy matching with a high threshold
        normalized_title = normalize_text(title)
        normalized_author_name = normalize_text(author_name)
        result = self.session.query(BookModel).filter(BookModel.normalized_title == normalized_title, BookModel.authors.any(AuthorModel.normalized_name == normalized_author_name)).first()
        if result:
            return self._create_book_from_db_result(result)
        
    def add_book(self, book: Book) -> Book:
        """
        Add a book to the repository.
        :param book: The book object to add.
        :return: The added book object.
        """
        existing_book = self.get_book_by_id(book.id)
        if existing_book:
            return existing_book
        self.session.add(self._create_book_model_from_domain_model(book))
        self.session.commit()

    def update_book(self, book: Book) -> Book:
        """
        Update a book.
        :param book: The book object to update.
        :return: The updated book object.
        """
        self.session.query(BookModel).filter(BookModel.id == book.id).update({
            BookModel.average_love_rating: book.average_love_rating,
            BookModel.average_shit_rating: book.average_shit_rating,
            BookModel.number_of_ratings: book.number_of_ratings,
            BookModel.sum_of_love_ratings: book.sum_of_love_ratings,
            BookModel.sum_of_shit_ratings: book.sum_of_shit_ratings
        })
        self.session.commit()

    def search_books(self, query: str, page_size: int, page: int = 1) -> list[Book]:
        """
        Search for books by title. Note that we return one more book than the page size to check if there are more books.
        :param query: The query to search for.
        :param page_size: The number of books per page.
        :param page: The page number to retrieve.
        :param threshold: The threshold for the similarity search.
        :return: A list of book objects.
        """
        # TODO: ts matches exactly on tokens, so it doesn't allow for spelling mistakes etc. 
        # Consider using trigram as a fallback or move to a dedicated search service (e.g. typesense)
        result = (self.session.query(BookModel)
            .filter(func.to_tsvector('english', BookModel.title)
                .op('@@')(func.plainto_tsquery('english', query)))
            .order_by(func.ts_rank(
                func.to_tsvector('english', BookModel.title),
                func.plainto_tsquery('english', query)
                ).desc())
            .offset((page - 1) * page_size)
            .limit(page_size + 1)
            .all())
        return [self._create_book_from_db_result(book) for book in result]
