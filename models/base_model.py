#!/usr/bin/env python3
"""This file contains the base class BaseModel for the AirBnB clone."""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    A class BaseModel that defines all common attributes/methods
    for other classes.

    Class Attributes:
    Methods:
    """

    def __init__(self, *args, **kwargs):
        """Instantiates the class BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue;
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        string representation of the class that prints using the format
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance.

        """
        obj_dict = self.__dict__
        obj_dict['__class__'] =  self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
