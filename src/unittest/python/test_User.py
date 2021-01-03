from unittest import TestCase
from src.main.python.User import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User('Hina', 'admin')

    def test_student_professors_actions(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.user.student_professors_actions()
        self.assertEqual(type(e.exception), FileNotFoundError)

    def test_admin_actions(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.user.admin_actions()
        self.assertEqual(type(e.exception),FileNotFoundError)
