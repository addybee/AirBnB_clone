#!/usr/bin/env python3
""" defines a class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
"""

from models import base_model
import json


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
        key = f"{type(obj)}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({key: val for key, val in self.__objects.items()}, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for key, val in self.__objects.items():
                    class_name = key.split(".")[0]
                    obj_class = getattr(base_model, class_name)
                    obj = obj_class(**val)
                    self.new(obj)
        except FileNotFoundError:
            pass
