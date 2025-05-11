from uuid import UUID

class Rating:
    def __init__(self, id: UUID, book_id: UUID, user_id: UUID, rating: float):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.rating = rating

class Book:
    def __init__(self, id: UUID, title: str, author: str):
        self.id = id
        self.title = title
        # TODO: author will be its own entity (authors might share names, have descriptions and other data)
        self.author = author
        # TODO: we'll likely track an average rating
        self.ratings = list[Rating] = []

    # TODO: check if the user already rated the book
    def rate(self, user_id: UUID, rating: Rating):
        self.ratings.append(rating)