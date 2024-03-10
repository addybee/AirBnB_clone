#!/usr/bin/python3
"""Test file for FileStorage unit testing"""


import pep8
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""

    def setUp(self):
        """Set up for testing FileStorage"""
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """
        Cleans up after json representation has been tested in test_file.json
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_base_pep8(self):
        """ test for pep8(pycodestyle) compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ test docstring in this current module """
        self.assertIsNotNone(__import__("models.engine.file_storage").__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_fileStorageExixtence(self):
        """Tests for the existence of  FileStorage class"""
        storage_obj = FileStorage()
        self.assertIsNotNone(storage_obj)

    def test_attribute_existence(self):
        """Test if public instance methods exist in FileStorage"""
        self.assertTrue(hasattr(self.storage, 'all'))
        self.assertTrue(hasattr(self.storage, 'new'))
        self.assertTrue(hasattr(self.storage, 'save'))
        self.assertTrue(hasattr(self.storage, 'reload'))

    def test_fileStorageMethods(self):
        """Test if all() returns a dictionary object"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_fileStorageInstance(self):
        """Test if private instance class exits in FileStorage"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new_fileStorageMethod(self):
        """Test if newly created objects sets the private object correctly"""
        my_model = BaseModel()
        self.storage.new(my_model)
        obj_key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertIn(obj_key, self.storage._FileStorage__objects)

    def test_serialised_json_obj(self):
        """Test if FileStorage objs added to __objects can be found there"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
            self.assertIn("BaseModel." + obj.id, data)

    def test_serialised_json_obj_reload(self):
        """
        Test if FileStorage objs when deleted and reloaded
        can be found in __objects
        """
        storage = FileStorage()
        obj = BaseModel()
        key = f"BaseModel.{obj.id}"
        storage.new(obj)
        storage.save()
        storage1 = FileStorage()
        storage1.reload()
        self.assertIn(key, storage1._FileStorage__objects)
        self.assertDictEqual(storage.all(), storage1.all())

    def test_reloadActionOn_File_Inexistence(self):
        """Test if reload doesn't perform any action if file doesn't exists"""
        storage = FileStorage()
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertDictEqual(storage.all(), {})


if __name__ == "__main__":
    unittest.main()
