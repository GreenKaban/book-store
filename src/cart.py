from typing import List

from src.book import Book


class Cart:
    def __init__(self):
        self._books: List[Book, ...] = []

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError(f'{book} is not Book')
        self._books.append(book)

    def delete_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError(f'{book} is not Book')
        if book in self._books:
            self._books.remove(book)
        else:
            raise ValueError(f'{book} is not in cart')

    @property
    def books(self):
        return self._books.copy()
