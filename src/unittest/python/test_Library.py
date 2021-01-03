from unittest import TestCase

from src.main.python.Library import Register
from src.main.python.Library import Login


class TestRegister(TestCase):

    def setUp(self):
        self.reg = Register('Hina', 'hina1234', 'hina1234@gmail.com', 'admin')

    def test_register_user(self):
        self.assertEqual(self.reg.username, 'Hina')
        self.assertEqual(self.reg.password, 'hina1234')
        self.assertEqual(self.reg.email, 'hina1234@gmail.com')
        self.assertEqual(self.reg.type, 'admin')

    def test_check_validation(self):
        self.reg = Register('Hina', '1234', 'hina1234@gmail.com', 'admin')
        with self.assertRaises(Exception) as e:
            self.reg.check_validation()
        self.assertTrue(type(e.exception) in [Exception])
        self.assertEqual(e.exception.args[0], "Invalid password!!")


class TestLogin(TestCase):
    def setUp(self):
        self.log = Login('Hina', 'hina1234')

    def test_user_condition(self):
        self.assertTrue(self.log.user_condition('Hina', 'hina1234'))
        self.assertFalse(self.log.user_condition('Hina', 'hina8765'))

    def test_check_user(self):
        with self.assertRaises(FileNotFoundError) as e:
            self.log.check_user()
        self.assertEqual(type(e.exception), FileNotFoundError)
