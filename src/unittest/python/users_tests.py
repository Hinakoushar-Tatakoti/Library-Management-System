from unittest import TestCase
from User import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User('Hina', 'admin')

    def test_admin_actions(self):
        try:
            self.user.admin_actions()
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)
