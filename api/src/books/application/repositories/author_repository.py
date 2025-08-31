from abc import ABC, abstractmethod

from sqlalchemy import UUID
from sqlalchemy.orm import Session

from src.books.domain.models import Author
from src.books.application.models import AuthorModel
from src.infrastructure.utilities.text_normalizer import normalize_text

class AbstractAuthorRepo(ABC):
    @abstractmethod
    def get_author_by_id(self, author_id: UUID) -> Author:
        pass

    @abstractmethod
    def get_author_by_name(self, name: str) -> Author:
        pass

    @abstractmethod
    def add_author(self, author: Author) -> Author:
        pass
    

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
        normalized_name = normalize_text(name)
        result = self.session.query(AuthorModel).filter(AuthorModel.normalized_name == normalized_name).first()
        if result:
            return self._create_author_from_db_result(result)

    def add_author(self, author: Author) -> Author:
        normalized_name = normalize_text(author.name)
        existing_author = self.get_author_by_name(normalized_name)
        if existing_author:
            return existing_author
        self.session.add(self._create_author_model_from_domain_model(author, normalized_name))
        self.session.commit()
    
