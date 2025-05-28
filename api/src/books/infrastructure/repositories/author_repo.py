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
    
    def _create_author_model_from_domain_model(self, author: Author) -> AuthorModel:
        return AuthorModel(
            id=author.id,
            name=author.name
        )

    def get_author_by_id(self, author_id: UUID) -> Author:
        result = self.session.query(AuthorModel).filter(AuthorModel.id == author_id).first()
        if result:
            return self._create_author_from_db_result(result)

    # TODO: authors can have the same name, we need a better way to distinguish them when querying external api
    # TODO: authors can be identified by different names (e.g. J.K. Rowling and Joanne Rowling), need to figure that one out 
    def get_author_by_name(self, name: str) -> Author:
        result = self.session.query(AuthorModel).filter(AuthorModel.name == name).first()
        if result:
            return self._create_author_from_db_result(result)

    def add_author(self, author: Author) -> Author:
        existing_author = self.get_author_by_name(author.name)
        if existing_author:
            return existing_author
        self.session.add(self._create_author_model_from_domain_model(author))
        self.session.commit()
        
