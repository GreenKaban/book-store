import unittest

from src.book import Book, Genre
from src.cart import Cart


def test_add_book(test_case, obj):
    with test_case.assertRaises(TypeError):
        obj.add_book('smth')

    book = Book(10., 'title', Genre.NOVEL)
    obj.add_book(book)

    books = obj.books
    test_case.assertEqual(len(books), 1)
    test_case.assertEqual(books[0], book)

    another_book = Book(10., 'title2', Genre.COMEDY)

    obj.add_book(another_book)

    books = obj.books
    test_case.assertEqual(len(books), 2)
    test_case.assertEqual(books[0], book)
    test_case.assertEqual(books[1], another_book)

class CartTest(unittest.TestCase):

    def test_add_book(self):
        cart = Cart()
        test_add_book(self, cart)

    def test_delete_book(self):
        cart = Cart()
        book = Book(10., 'title', Genre.NOVEL)
        another_book = Book(10., 'title2', Genre.COMEDY)
        cart.add_book(book)
        cart.add_book(another_book)

        with self.assertRaises(TypeError):
            cart.delete_book('smth')

        random_book = Book(11., 'title', Genre.NOVEL)
        with self.assertRaises(ValueError):
            cart.delete_book(random_book)

        cart.delete_book(book)

        books = cart.books
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0], another_book)
