#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If a class is specified, returns objects of that class.
        """
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside.
        If obj is None, does nothing.
        """
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
