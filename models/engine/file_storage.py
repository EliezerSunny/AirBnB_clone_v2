import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects or objects of a specific class"""
        if cls:
            filtered_objects = {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
            return filtered_objects
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is None:
            return
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        if obj_key in self.__objects:
            del self.__objects[obj_key]
            self.save()
