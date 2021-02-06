from unittest import TestCase
from Books import Books


class TestBooks(TestCase):

    def test_display_books(self):
        try:
            self.bk = Books('Hina')
            self.bk.display_books()
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)
