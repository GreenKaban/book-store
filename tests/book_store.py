import unittest

from book import Book, Genre
from cart import Cart
from src.book_store import BookStore
from tests.cart import test_add_book


class BookStoreTest(unittest.TestCase):

    def test_add_book(self):
        book_store = BookStore([])
        test_add_book(self, book_store)

    def test_get_receipt(self):
        cart = Cart()
        book = Book(10., 'title', Genre.NOVEL)
        another_book = Book(10., 'title2', Genre.COMEDY)
        cart.add_book(book)

        book_store = BookStore([])

        with self.assertRaises(ValueError):
            book_store.get_receipt(cart)

        book_store.add_book(book)
        price = book_store.get_receipt(cart)
        self.assertEqual(price, 10.)

        cart.add_book(another_book)
        book_store.add_book(another_book)

        price = book_store.get_receipt(cart)
        self.assertEqual(price, 10. * 2 * 0.95)
