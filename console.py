#!/usr/bin/python3
"""
describe the class that contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
from models import storage
from re import search
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


class HBNBCommand(cmd.Cmd):
    """Defines a command processor."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """
        Hook method that will be called when the user enters the end-of-file
        character.
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it(to the JSON)
        and prints the id.
        """
        if not args:
            print("** class name missing **")
        elif args in class_dict.keys():
            cls_name = class_dict[args]
            obj = cls_name()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class
        name and id
        """
        args = args.split(" ")
        argc = len(args)

        if argc == 2 and search(r'^"*[\w-]*"$', args[1]):
            args[1] = args[1].strip('"')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 2 and not args[1]:
            print("** instance id missing **")
        else:
            key = ".".join(args[:2]) 
            db = storage.all()
            if key in db.keys():
                print(db[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        args = args.split(" ")
        argc = len(args)

        if argc == 2 and search(r'^"*[\w-]*"$', args[1]):
            args[1] = args[1].strip('"')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = ".".join(args)
            db = storage.all()
            if key in db.keys():
                del db[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        db = storage.all()
        list_all = []
        if not args:
            for obj in db.values():
                list_all.append(str(obj))
        else:
            if args not in class_dict.keys():
                print("** class doesn't exist **")
                return
            else:
                for key, val in db.items():
                    if key.split(".")[0] == args:
                        list_all.append(str(val))
        print(list_all)


    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = args.split(" ")
        args_length = len(args)
        if args_length > 1:
            db = storage.all()
            key = "{}.{}".format(args[1])

        if not args[0]:
            print("** class name missing **")
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif args_length < 2:
            print("** instance id missing **")
        elif key not in db.keys():
            print("** no instance found **")
        elif args_length < 3:
            print("** attribute name missing **")
        elif args_length < 4:
            print("** value missing **")
        else:
            if search(r"^\d+\.\d+$", args[3]):
                args[3] = float(args[3])
            elif search(r"^\d+$", args[3]):
                args[3] = int(args[3])
            elif search(r"^\"\w*\"$", args[3]):
                args[3] = args[3].strip("\"")

            setattr(db[key], args[2], args[3])
            db[key].save()

    def do_count(self, args):
        """
        retrieve the number of instances of a class
        usage:
            <class name>.count()
        """
        if not args:
            print("** class name missing **")
        elif args in class_dict.keys():
            counter = 0
            for key in storage.all().keys():
                if key.split(".")[0] == args:
                    counter += 1
            print(counter)
        else:
            print("** class doesn't exist **")

    def default(self, args):
        """ handles undefined commands """
        argv = args.split(".")
        argc = len(argv)

        if argc == 2:
            if argv[0] in class_dict.keys():
                if argv[1] == "all()":
                    self.do_all(argv[0])
                    return
                elif argv[1] == "count()":
                    self.do_count(argv[0])
                    return
                elif search(r'^show\("[\w-]*"\)$', argv[1]):
                    id = argv[1].strip('show(').strip(')')
                    name_id = "{} {}".format(argv[0], id)
                    self.do_show(name_id)
                    return
                elif search(r'^destroy\("[\w-]*"\)$', argv[1]):
                    id = argv[1].strip('destroy(').strip(')')
                    name_id = "{} {}".format(argv[0], id)
                    self.do_destroy(name_id)
                    return
            else:
                if search(r'^show\("[\w-]*"\)$', argv[1]):
                    id = argv[1].strip('show("').strip('")')
                    name_id = "{} {}".format(argv[0], id)
                    self.do_show(name_id)
                    return
                elif search(r'^destroy\("[\w-]*"\)$', argv[1]):
                    id = argv[1].strip('destroy(').strip(')')
                    name_id = "{} {}".format(argv[0], id)
                    self.do_destroy(name_id)
                    return

        print('*** Unknown syntax: {}'.format(args))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
