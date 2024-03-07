#!/usr/bin/env python3
""" defines a class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
"""


from models.base_model import BaseModel
from models.user import User
import json
import os
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to
    instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        if not self.__file_path:
            return
        json_obj = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_obj, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                result = json.load(f)
            for key, val in result.items():
                class_name = globals()[key.split(".")[0]]
                obj = class_name(**val)
                FileStorage.__objects[key] = obj
