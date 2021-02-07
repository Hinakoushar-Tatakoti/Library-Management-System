from unittest import TestCase
from src.main.python.User import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User('Hina', 'admin')

    def test_student_professors_actions(self):
        try:
            self.user.student_professors_actions()
        except ValueError:
            self.assertRaises(ValueError)

    def test_admin_actions(self):
        try:
            self.user.admin_actions()
        except ValueError:
            self.assertRaises(ValueError)
