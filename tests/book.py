import unittest

from src.book import Genre, Book


class BookTest(unittest.TestCase):

    def test_book_invalid_type(self):
        with self.assertRaises(TypeError):
            Book(price='qwe', title='qwe', genre=Genre.NOVEL)

        with self.assertRaises(TypeError):
            Book(price=10., title=1, genre=Genre.NOVEL)

        with self.assertRaises(TypeError):
            Book(price=10., title='qwe', genre='qwe')

        with self.assertRaises(ValueError):
            Book(price=-10., title='qwe', genre=Genre.NOVEL)

    def test_valid(self):
        price = 10.
        title = 'qwe'
        genre = Genre.NOVEL
        book = Book(price=price, title=title, genre=genre)
        self.assertEqual(price, book.price)
        self.assertEqual(title, book.title)
        self.assertEqual(genre, book.genre)

