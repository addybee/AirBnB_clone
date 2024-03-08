#!/usr/bin/python3
"""
defines a class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    inherits from BaseModel
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
