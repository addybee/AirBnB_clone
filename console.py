#!/usr/bin/python3


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


class HBNBCommand(cmd.Cmd):
    """Defines a command processor."""

    prompt = '(hbnb) '
    file_path = 'file.json'
    list_of_classes = ["BaseModel", "User", "State", "City",
                       "Amenity", "Place", "Review"]

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it(to the JSON)
        and prints the id.
        """
        if not args:
            print("** class name missing **")
        elif args in self.list_of_classes:
            args = args.strip()
            cls_name = globals()[args]
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
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in self.list_of_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = ".".join(args)
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
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in self.list_of_classes:
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
            if args not in self.list_of_classes:
                print("** class doesn't exist **")
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
            key = ".".join(args[:2])

        if not args[0]:
            print("** class name missing **")
        elif args[0] not in self.list_of_classes:
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

    def do_EOF(self, line):
        """
        Hook method that will be called when the user enters the end-of-file
        character.
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def postloop(self):
        """ print a newline character """
        pass

    def cmdloop(self):
        try:
                super().cmdloop()
        except KeyboardInterrupt:
                print("^D")   # Handle Ctrl+D gracefully
    
    def completedefault(self, text, line, begidx, endidx):
        """Provide completion suggestions for unrecognized commands."""
        commands = ['create', 'quit', 'help', 'show', 'destroy', 'update',
                    'all']  # List of known commands
        # Filter commands based on the prefix 'text'
        return [cmd for cmd in commands if cmd.startswith(text)]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
