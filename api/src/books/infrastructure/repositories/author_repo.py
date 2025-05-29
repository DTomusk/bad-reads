import re
import unicodedata
from sqlalchemy import UUID
from sqlalchemy.orm import Session

from src.books.domain.models import Author
from src.books.infrastructure.models import AuthorModel
from src.books.application.repositories.author_repository import AbstractAuthorRepo

class AuthorRepo(AbstractAuthorRepo):
    def __init__(self, session: Session):
        self.session = session

    def _create_author_from_db_result(self, result: AuthorModel) -> Author:
        return Author(
            id=result.id,
            name=result.name
        )
    
    def _create_author_model_from_domain_model(self, author: Author, normalized_name: str) -> AuthorModel:
        return AuthorModel(
            id=author.id,
            name=author.name,
            normalized_name=normalized_name
        )

    def get_author_by_id(self, author_id: UUID) -> Author:
        result = self.session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if result:
            return self._create_author_from_db_result(result)

    def get_author_by_name(self, name: str) -> Author:
        result = self.session.query(AuthorModel).filter(AuthorModel.normalized_name == name).first()
        if result:
            return self._create_author_from_db_result(result)

    def add_author(self, author: Author) -> Author:
        normalized_name = self._normalize_author_name(author.name)
        existing_author = self.get_author_by_name(normalized_name)
        if existing_author:
            return existing_author
        self.session.add(self._create_author_model_from_domain_model(author, normalized_name))
        self.session.commit()

    # TODO: this needs tests
    def _normalize_author_name(self, name: str) -> str:
        # Lowercase
        name = name.lower()
        
        # Normalize unicode (e.g., é → e)
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
        
        # Remove punctuation
        name = re.sub(r'[^\w\s]', '', name)
        
        # Remove extra whitespace
        name = re.sub(r'\s+', ' ', name).strip()
        
        # Optionally: Combine single-letter initials (e.g., "j k rowling" → "jk rowling")
        name = re.sub(r'\b(\w)\s+(?=\w\b)', r'\1', name)

        return name