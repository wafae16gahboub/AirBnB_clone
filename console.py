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

    allClasses = {
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
        args = line.split()
        className = None
        id = None

        try:
            className = args[0]
        except IndexError:
            pass
        if not self.checkClassName(className):
            return

        try:
            id = args[1]
        except IndexError:
            pass

        if id is None:
            print("** instance id missing **")
            return
        objs = storage.all()
        idsList = []
        for key in objs.keys():
            if key.startswith(args[0]):
                idsList.append(key.split(".")[1])

        if id not in idsList:
            print("** no instance found *")
            return

        print(objs[f"{className}.{id}"])

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
        elif className not in self.allClasses:
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
        elif className not in self.allClasses:
            print("** class doesn't exist **")
            return False
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass
    def do_destroy(self, ligne):
        """destroy:00000"""
        if len(ligne) == 0:
            print("** class name missing **")
        else:
            ligne = ligne.split()
            if ligne[0] in models.class_dict:
                try:
                    obj_id = ligne[0] + '.' + ligne[1]
                except IndexError:
                    print(("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
