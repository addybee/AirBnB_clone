#!/usr/bin/python3
"""
defines the unittest class for Place
"""


import pep8
from datetime import datetime
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ describes the test for User model """
    def setUp(self):
        """ initial setup before each test in TestBaseModel """
        self.model = Place()

    def tearDown(self):
        """ clean up after each test """
        del self.model

    def test_base_pep8(self):
        """ test for pep8(pycodestyle) compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """ test docstring in this current module """
        self.assertIsNotNone(__import__("models.place").__doc__)
        self.assertIsNotNone(Place.__doc__)

    def test_present_attributes(self):
        """ test the attributes presence and type """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertTrue(hasattr(self.model, 'city_id'))
        self.assertTrue(hasattr(self.model, 'user_id'))
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'description'))
        self.assertTrue(hasattr(self.model, 'number_rooms'))
        self.assertTrue(hasattr(self.model, 'number_bathrooms'))
        self.assertTrue(hasattr(self.model, 'max_guest'))
        self.assertTrue(hasattr(self.model, 'latitude'))
        self.assertTrue(hasattr(self.model, 'longitude'))
        self.assertTrue(hasattr(self.model, 'amenity_ids'))
        self.assertTrue(hasattr(self.model, 'price_by_night'))

    def test_instance_of_the_attributes(self):
        """ check the user attribute type instance """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsInstance(self.model.city_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.description, str)
        self.assertIsInstance(self.model.number_rooms, int)
        self.assertIsInstance(self.model.number_bathrooms, int)
        self.assertIsInstance(self.model.max_guest, int)
        self.assertIsInstance(self.model.price_by_night, int)
        self.assertIsInstance(self.model.latitude, float)
        self.assertIsInstance(self.model.longitude, float)
        self.assertIsInstance(self.model.amenity_ids, list)

    def test_attribute_init_values(self):
        """ test the initialization value to empty string """
        self.assertEqual(self.model.city_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.description, "")
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        self.assertEqual(self.model.latitude, 0.0)
        self.assertEqual(self.model.longitude, 0.0)
        self.assertListEqual(self.model.amenity_ids, [])

    def test_class_subclass(self):
        """ test the subclass of object and the class it belongs"""
        self.assertIsInstance(self.model, Place)
        self.assertTrue(issubclass(self.model.__class__, BaseModel))

    def test_save_method(self):
        """ test the save method """
        var_update = self.model.updated_at
        self.model.save()
        self.assertNotEqual(var_update, self.model.updated_at)

    def test_from_dict_to_obj(self):
        """ test the conversion from dict to object(User) """
        new_dict = self.model.to_dict()
        new_model = Place(**new_dict)
        self.assertDictEqual(new_model.to_dict(), new_dict)
        self.assertIsInstance(new_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
