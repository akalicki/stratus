"""
    stratus.py
"""

import readline, os
from lib import *

print "\nstratus.py - Unlimited cloud storage!" 
print "Enter a command, or type 'help' to get started.\n"

running = True
while running:
    cmd = raw_input('> ')
    if cmd == 'help':
        print "\nstratus.py - v0.1.0"
        print "---------------------"
        print "help   - list all commands"
        print "logout - exit the program (aliases: exit, quit)\n"
    elif cmd == 'exit' or cmd == 'logout' or cmd == 'quit':
        running = False
    else:
        print "\nNot a valid command."
        print "Enter a valid command or type 'help' to get started.\n"