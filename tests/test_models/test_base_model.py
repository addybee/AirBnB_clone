#!/usr/bin/env python3

"""
This is the test suit for the AirBnB class BaseModel.
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

   

    def test_created_at_updated_at(self):
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_kwargs(self):
        kwargs = {
            'name': 'My First Model',
            'my_number': 89,
            'created_at': '2024-03-08 01:27:35.435310',
            'updated_at': '2024-03-08 01:27:35.435311'
        }

        my_model = BaseModel(**kwargs)
        self.assertIsInstance(my_model.name, str)
        self.assertIsInstance(my_model.my_number, int)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_empty_kwargs(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertFalse(hasattr(my_model, 'name'))
        self.assertFalse(hasattr(my_model, 'my_number'))
        self.assertFalse(hasattr(my_model, 'updated_at'))

    def test_str_display(self):
        str_should_print = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                        self.my_model.__dict__)
        self.assertEqual(str(self.my_model), str_should_print)

    def test_save_updated_at(self):
        initial_update_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_update_at, self.my_model.updated_at)

    def test_invalid_argument(self):
        invalid_key = 'invalid_attribute'
        invalid_value = 'invalid_value'
        model_dict_repr = self.my_model.to_dict()

        self.assertNotIn(invalid_key, model_dict_repr.keys())
        for key, value in model_dict_repr.items():
            self.assertNotEqual(value, invalid_value)

    def test_to_dict(self):
        model_dict_repr = self.my_model.to_dict()
        self.assertIsInstance(model_dict_repr, dict)
        self.assertIn('__class__', model_dict_repr)
        self.assertEqual(model_dict_repr['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict_repr)
        self.assertIn('updated_at', model_dict_repr)
        self.assertTrue(any(isinstance(model_dict_repr[key], str)
                            for key in ['created_at', 'updated_at']))


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""

    def setUp():
        self.storage = FileStorage()

    def test_fileStorageMethods(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_fileStorageInstance(self):
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)


if __name__ == "__main__":
    unittest.main()
