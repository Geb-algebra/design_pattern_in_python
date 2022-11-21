"""
どんなパターンか：
いつ使うか：
何が嬉しいか：
"""

from __future__ import annotations
from typing import Any


class Iterable:
    """Interface for iterable classes"""

    def iterator(self) -> Iterator:
        """Create an Iterator instance for this iterable"""
        pass


class Iterator:
    """Interface for iterator classes"""

    def has_next(self) -> bool:
        """whether this iterator can go to the next element

        Returns:
            bool: whether this iterator can go to the next element
        """
        pass

    def next(self) -> Any:
        """return the element on which this iterator is and go to next element

        Returns:
            Any: _description_
        """
        pass


class Book:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self) -> str:
        return self._name


class BookshelfIterator(Iterator):
    def __init__(self, bookshelf: Bookshelf):
        self.bookshelf = bookshelf
        self.index = 0

    def next(self) -> Book:
        return_book = self.bookshelf[self.index]
        self.index += 1
        return return_book

    def has_next(self) -> bool:
        try:
            self.bookshelf[self.index]
            return True
        except IndexError:
            return False


class Bookshelf(Iterable):
    def __init__(self, books: list[Book]):
        self.books = books

    def iterator(self):
        return BookshelfIterator(self)

    def __getitem__(self, index: int):
        return self.books[index]


def main(books: list[Book]):
    """
    Iteratorを介してループを回すことで、Iteratorインターフェイスのメソッドしか使わずに済む
    これにより、bookshelfの実装に依存せずにループを回せる。
    """
    bookshelf = Bookshelf(books)
    bi = bookshelf.iterator()
    while bi.has_next():
        print(bi.next())


if __name__ == "__main__":
    books = [Book("book1"), Book("book2"), Book("book3")]
    main(books)
