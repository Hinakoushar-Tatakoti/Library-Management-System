from unittest import TestCase
from src.main.python.Books import Books


class TestBooks(TestCase):
    def setUp(self):
        self.bk = Books('Hina')

    def test_display_books(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.display_books()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_borrow_book(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.borrow_book()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_return_book(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.return_book()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_check_fine(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.check_fine()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_search_by_name(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.searchByName()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_add_book(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.add_book()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_remove_book(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.bk.remove_book()
        self.assertEqual(type(e.exception), FileNotFoundError)
