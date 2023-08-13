#!/usr/bin/python3
"""BaseModel class"""
import uuid
import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """_summary_
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        theformat = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.datetime.strptime(
                            str(value), theformat)
                    setattr(self, key.lower(), value)
        else:
            models.storage.new(self)

    def save(self):
        """_summary_
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            **self.__dict__,
            "__class__": type(self).__name__,
            "created_at": self.created_at.isoformat("T"),
            "updated_at": self.updated_at.isoformat("T"),
        }

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
