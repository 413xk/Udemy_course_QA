# Here is about hinting in functions

from typing import List # , Tuple, Set, etc


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


list_avg(123)


class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'Book {self.name}, {self.book_type}, weighing {self.weight}'

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book": # will return object Book. If class is not over, use "" to return object
        return cls(name, cls.TYPES[0], page_weight + 100)