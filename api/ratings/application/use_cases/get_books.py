from api.ratings.application.repositories.book_repository import BookRepo


class GetBooks:
    def __init__(self, book_repository: BookRepo):
        self.book_repository = book_repository

    def execute(self):
        return self.book_repository.get_books()