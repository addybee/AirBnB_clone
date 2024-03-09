#!/usr/bin/python3
"""Test file for FileStorage unit testing"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import os
import json


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""

    def setUp(self):
        """Set up for testing FileStorage"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """
        Cleans up after json representation has been tested in test_file.json
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

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
        self.assertEqual(self.storage._FileStorage__file_path, "test_file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_new_fileStorageMethod(self):
        """Test if newly created objects sets the private object correctly"""
        my_model = BaseModel()
        self.storage.new(my_model)
        obj_key = "{} {}".format(type(my_model).__name__, my_model.id)
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
        storage.new(obj)
        storage.save()
        storage._FileStorage__objects = {}

        storage.reload()

        self.assertIn("BaseModel." + obj.id, storage._FileStorage__objects)

    def test_reloadActionOn_File_Inexistence(self):
        """Test if reload doesn't perform any action if file doesn't exixts"""
        storage = FileStorage()
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

        storage.reload()
        self.assertDictEqual(storage.all(), {})


if __name__ == "__main__":
    unittest.main()
