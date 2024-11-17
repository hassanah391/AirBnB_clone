#!/usr/bin/python3
"""

Module review has a class called Review that inherits from
Basemodel class 
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
    
