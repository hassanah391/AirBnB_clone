#!/usr/bin/python3
"""

Module file_storage has 
a class FileStorage  that serializes instances to a JSON file 
and deserializes JSON file to instances:
"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_dic = {}

        for key, obj in self.__objects.items():
            my_dic[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(my_dic, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
                for key, value in new_obj.items():
                    obj = self.class_dict[value['__class__']](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass