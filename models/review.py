#!/usr/bin/env python3
'''
    define class "Review" and their attributes
'''


from models.base_model import BaseModel


class Review(BaseModel):
        """ descibes Review attributes and methods"""
        place_id = ""
        user_id = ""
        text = ""
