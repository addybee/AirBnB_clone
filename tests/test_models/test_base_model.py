#!/usr/bin/python3
"""
This is the test suit for the AirBnB class BaseModel.
"""


from uuid import uuid4
import pep8
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def setUp(self):
        """ initial setup before each test in TestBaseModel """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_base_pep8(self):
        """ test for pep8(pycodestyle) compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ test docstring in this current module """
        self.assertIsNotNone(__import__("models.base_model").__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_BaseModel_attribute(self):
        """ test the attributes presence and type """
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
    
    def test_from_dict_to_obj(self):
        """ test the conversion from dict to object(BaseModel) """
        new_dict = self.my_model.to_dict()
        new_model = BaseModel(**new_dict)
        self.assertDictEqual(new_model.to_dict(), new_dict)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_init_no_args(self):
        """ test id uniqueness, compare the updated_at"""
        n_model = BaseModel()
        self.assertNotEqual(n_model.id, self.my_model.id)
        self.assertLess(n_model.created_at, datetime.now())
        self.assertEqual(n_model.updated_at.second, n_model.created_at.second)

    def test_str_display(self):
        """ test the str method """
        str_should_print = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                        self.my_model.__dict__)
        self.assertEqual(str(self.my_model), str_should_print)

    def test_save(self):
        """ test save method """
        initial_update_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_update_at, self.my_model.updated_at)

    def test_invalid_argument(self):
        """ test for invalid attributes """
        invalid_key = 'invalid_attribute'
        invalid_value = 'invalid_value'
        model_dict_repr = self.my_model.to_dict()

        self.assertNotIn(invalid_key, model_dict_repr.keys())
        for key, value in model_dict_repr.items():
            self.assertNotEqual(value, invalid_value)

    def test_to_dict(self):
        """ test to dicttionary """
        model_dict_repr = self.my_model.to_dict()
        self.assertIsInstance(model_dict_repr, dict)
        self.assertIn('__class__', model_dict_repr)
        self.assertEqual(model_dict_repr['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict_repr["created_at"], str)
        self.assertIsInstance(model_dict_repr["updated_at"], str)
        self.assertIn('created_at', model_dict_repr)
        self.assertIn('updated_at', model_dict_repr)
        self.assertTrue(any(isinstance(model_dict_repr[key], str)
                            for key in ['created_at', 'updated_at']))


if __name__ == "__main__":
    unittest.main()
