#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines a command processor."""
    
    prompt = '(hbnb) '
    file_path = 'file.json'

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it(to the JSON)
        and prints the id.
        """
        if not args:
            print("** class name missing **")
            return

        try:
            classname = args.strip()
            from_file = __import__("__main__")
            cls_name = getattr(from_file, classname)
            obj = cls_name()

            with open(self.file_path, 'r+') as f:
                data = json.load(f)
                obj_dict = obj.to_dict()
                data[obj_dict['__class__'] + '.' + obj_dict['id']] = obj_dict
                f.seek(0)
                json.dump(data, f)

            print(obj_dict['id'])

        except AttributeError:
            print("** class doesn't exist **")

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
