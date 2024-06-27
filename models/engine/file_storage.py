#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the list of objects of one type of class"""
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
            for key in json_objects:
                cls_name = key.split('.')[0]
                if cls_name in classes:
                    self.__objects[key] = classes[cls_name](**json_objects[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
