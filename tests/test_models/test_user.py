#!/usr/bin/python3
"""
defines the unittest class for User
"""


import pep8
from datetime import datetime
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ describes the test for User model """
    def setUp(self):
        """ initial setup before each test in TestBaseModel """
        self.model = User()

    def tearDown(self):
        """ clean up after each test """
        del self.model

    def test_base_pep8(self):
        """ test for pep8(pycodestyle) compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ test docstring in this current module """
        self.assertIsNotNone(__import__("models.user").__doc__)
        self.assertIsNotNone(User.__doc__)

    def test_present_attributes(self):
        """ test the attributes presence and type """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertTrue(hasattr(self.model, 'email'))
        self.assertTrue(hasattr(self.model, 'password'))
        self.assertTrue(hasattr(self.model, 'first_name'))
        self.assertTrue(hasattr(self.model, 'last_name'))

    def test_instance_of_the_attributes(self):
        """ check the user attribute type instance """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsInstance(self.model.email, str)
        self.assertIsInstance(self.model.password, str)
        self.assertIsInstance(self.model.first_name, str)
        self.assertIsInstance(self.model.last_name, str)

    def test_attribute_init_values(self):
        """ test the initialization value to empty string """
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")

    def test_class_subclass(self):
        """ test the subclass of object and the class it belongs"""
        self.assertIsInstance(self.model, User)
        self.assertTrue(issubclass(self.model.__class__, BaseModel))

    def test_save_method(self):
        """ test the save method """
        var_update = self.model.updated_at
        self.model.save()
        self.assertNotEqual(var_update, self.model.updated_at)

    def test_from_dict_to_obj(self):
        """ test the conversion from dict to object(User) """
        new_dict = self.model.to_dict()
        new_model = User(**new_dict)
        self.assertDictEqual(new_model.to_dict(), new_dict)
        self.assertIsInstance(new_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
