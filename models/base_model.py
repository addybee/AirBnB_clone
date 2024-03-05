#!/usr/bin/env python3
"""This file contains the base class BaseModel for the AirBnB clone."""

from datetime import datetime
import uuid


class BaseModel:
    """
    A class BaseModel that defines all common attributes/methods
    for other classes.

    Class Attributes:
    Methods:
    """

    def __init__(self):
        """Instantiates the class BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        string representation of the class that prints using the format
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance.
        """
        return {
            'name': self.__dict__,
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'updated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            '__class__': __class__.__name__
        }
