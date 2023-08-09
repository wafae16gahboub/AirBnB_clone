#!/usr/bin/python3
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """_summary_
    """
    __file_path = "file.json"
    __objects = {}

    allClasses = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State,
    }

    def all(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return type(self).__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        type(self).__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """_summary_
        """
        objs = {
            key: value.to_dict() for key, value in type(self).__objects.items()
        }
        with open(self.__file_path, mode="w", encoding="utf-8") as f: 
            f.write(json.dumps(objs))
        pass

    def reload(self):
        """_summary_
        """
        try:
            with open(type(self).__file_path, mode="r", encoding="utf-8") as f:
                fileLoad = json.loads(f.read())
                for key, value in fileLoad.items():
                    obj = self.allClasses[value["__class__"]](**value)
                    self.__objects[key] = obj
        except:
            pass