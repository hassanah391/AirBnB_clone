#!/usr/bin/python3
"""
Module base_model has
a class BaseModel that is super class of all subclasses
that inhertes from it.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: random uuid, dates created/updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return string of info about model
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update instance with updated time & save to serialized file
        """
        self.updated_at = datetime.now()
        storage.save()

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def to_dict(self):
        """
        Return dic with string formats of times; add class info to dic
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
