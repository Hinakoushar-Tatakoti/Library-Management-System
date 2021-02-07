from unittest import TestCase
import unittest

from Library import Register, validate_user, validate_password, validate_email, validate_type, Login


class TestRegister(TestCase):

    def setUp(self):
        self.reg = Register('Hina', 'hina1234', 'hina1234@gmail.com', 'admin')

    def test_register_user(self):
        self.assertEqual(self.reg.username, 'Hina')
        self.assertEqual(self.reg.password, 'hina1234')
        self.assertEqual(self.reg.email, 'hina1234@gmail.com')
        self.assertEqual(self.reg.type, 'admin')


class TestValidations(TestCase):
    def test_validate_user(self):
        try:
            self.assertIsNone(validate_user("hina"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_password(self):
        try:
            self.assertTrue(validate_password("fgh"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_email(self):
        try:
            self.assertTrue(validate_email("fgh234"))
        except SystemExit:
            self.assertRaises(SystemExit)

    def test_validate_type(self):
        try:
            self.assertTrue(validate_type("user"))
        except SystemExit:
            self.assertRaises(SystemExit)


class TestLogin(TestCase):
    def setUp(self):
        self.log = Login('Hina', 'hina1234')

    def test_user_condition(self):
        self.assertTrue(self.log.user_condition('Hina', 'hina1234'))
        self.assertFalse(self.log.user_condition('Hina', 'hina8765'))

    def test_check_user(self):
        try:
            self.assertEqual(self.log.check_user(), "admin")
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError)

if __name__ == '__main__':
	unittest.main()