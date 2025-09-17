from enum import Enum


class BookSortOption(str, Enum):
    most_loved = "most_loved"
    most_poos = "most_poos"
    alphabetical = "alphabetical"