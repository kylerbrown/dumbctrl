from __future__ import print_function, unicode_literals, division
import zmq
from cmd import Cmd

import sys

PY_VERSION = sys.version_info[0]
if PY_VERSION >= 3:
    import configparser
else:
    import ConfigParser as configparser

def parse_parameters():
    """returns a parameter dictionary"""
    config = configparser.ConfigParser()
    config.read("parameters.ini")
    

class DumbShell(Cmd):
    intro = "Welcome to the dumb control shell. Type help or ? to list commands"
    prompt = "(dumb) "

    def do_status(self, *args):
        print("Everything is awesome!")
    def do_connect(self, *args):
        print("connecting to {}.".format(args[0]))


if __name__ == "__main__":
    # parameters to be set in a better way:
    GUIhost="localhost"
    port=5556
    d = DumbShell()
    d.cmdloop()

