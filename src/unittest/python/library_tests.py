from unittest import TestCase

from src.main.python.Errors import InvalidPasswordException, InvalidEmailException, InvalidTypeException, \
    InvalidUserException
from src.main.python.Library import Register, validate_user, validate_password, validate_email, validate_type
from src.main.python.Library import Login
from src.main.python.Library import Start


class TestRegister(TestCase):

    def setUp(self):
        self.reg = Register('Hina', 'hina1234', 'hina1234@gmail.com', 'admin')

    def test_register_user(self):
        self.assertEqual(self.reg.username, 'Hina')
        self.assertEqual(self.reg.password, 'hina1234')
        self.assertEqual(self.reg.email, 'hina1234@gmail.com')
        self.assertEqual(self.reg.type, 'admin')


class TestLogin(TestCase):
    def setUp(self):
        self.log = Login('Hina', 'hina1234')

    def test_user_condition(self):
        self.assertTrue(self.log.user_condition('Hina', 'hina1234'))
        self.assertFalse(self.log.user_condition('Hina', 'hina8765'))

    def test_check_user(self):
        self.assertEqual(self.log.check_user(), "admin")


class TestValidations(TestCase):
    def test_validate_user(self):
        try:
            self.assertTrue(validate_user("hina"))
        except InvalidUserException:
            self.assertRaises(InvalidUserException)

    def test_validate_password(self):
        try:
            self.assertTrue(validate_password("fgh"))
        except InvalidPasswordException:
            self.assertRaises(InvalidPasswordException)

    def test_validate_email(self):
        try:
            self.assertTrue(validate_email("fgh234"))
        except InvalidEmailException:
            self.assertRaises(InvalidEmailException)

    def test_validate_type(self):
        try:
            self.assertTrue(validate_type("user"))
        except InvalidTypeException:
            self.assertRaises(InvalidTypeException)


class Test(TestCase):

    def setUp(self):
        self.start = Start()

    def test_start(self):
        try:
            self.assertIsNone(self.start.actions())
        except SystemExit:
            self.assertRaises(SystemExit)
