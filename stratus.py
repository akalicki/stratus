"""
    stratus - v0.1.0
    Author: Alex Kalicki (https://github.com/akalicki)

    Free unlimited cloud storage!

    All work contained in this file is released under the MIT License.
    Please contact the copyright holder with further questions.
"""

import readline
from lib import *

def print_help():
    print "\nstratus - v0.1.0"
    print "---------------------"
    print "  help   - list all commands"
    print "  logout - exit the program (aliases: exit, quit)"
    navigate.print_help()
    dbox.print_help()
    print ""

print "\nstratus.py - Free unlimited cloud storage!" 
print "Enter a command, or type 'help' to get started.\n"

running = True
while running:
    user_input = raw_input('> ')
    args = user_input.split(' ')
    cmd = args[0]
    if cmd == 'help' and len(args) == 1:
        print_help()
    elif cmd in {'exit', 'logout', 'quit'} and len(args) == 1:
        running = False
    elif cmd in navigate.COMMANDS:
        navigate.process_command(args)
    elif cmd in dbox.COMMANDS:
        dbox.process_command(args)
    else:
        print "Error: '" + user_input + "' is not defined."
        print "Enter a valid command or type 'help' to get started."