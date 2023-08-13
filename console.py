#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    __allClasses = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State,
    }

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        className = None
        try:
            className = line.split()[0]
        except IndexError:
            pass

        if not self.checkClassName(className):
            return

        newInstance = self.allClasses[className]()
        print(newInstance.id)
        newInstance.save()

    def do_show(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.__allClasses:
            print("** class doesn't exist **")
            return
        try:
            objId = f"{args[0]}.{args[1]}"
        except IndexError:
            print("** instance id missing **")
            return

        try:
            print(storage.all()[objId])
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        className = None
        try:
            className = line.split()[0]
        except IndexError:
            pass

        objs = storage.all()
        if not className:
            for key in objs:
                print(objs[key])
        elif className not in self.__allClasses:
            print("** class doesn't exist **")
        else:
            for key in objs:
                if key.startswith(className):
                    print(objs[key])

    def checkClassName(self, className):
        """_summary_

        Args:
            className (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not className:
            print("** class name missing **")
            return False
        elif className not in self.__allClasses:
            print("** class doesn't exist **")
            return False
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_destroy(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in self.__allClasses:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        storage.save()
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        if len(line) == 0:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.__allClasses:
            print("** class doesn't exist **")
            return
        try:
            key = f"{args[0]}.{args[1]}"
        except IndexError:
            print("** instance id missing **")
            return

        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
