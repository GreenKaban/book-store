from typing import Iterable

from src.book import Book
from src.cart import Cart


class BookStore:
    def __init__(self, init_book: Iterable[Book]):
        if not all(isinstance(x, Book) for x in init_book):
            raise TypeError
        self._books = list(init_book)

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError(f'{book} is not Book')
        self._books.append(book)

    def get_receipt(self, cart: Cart):
        diff = set(cart.books) - set(self._books)
        if len(diff) > 0:
            raise ValueError(f'books: {diff} is not in store')

        price = sum(book.price for book in cart.books)
        if len(set(cart.books)) >= 2:
            price *= 0.95

        return price

    @property
    def books(self):
        return self._books.copy()
