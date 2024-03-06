#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines a command processor."""
    
    prompt = '(hbnb) '

    def do_create(self, name):
        """
        Creates a new instance of BaseModel, saves it(to the JSON)
        and prints the id.
        """
        if not name:
            print("** class name missing **")

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
