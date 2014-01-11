"""
    stratus // navigate.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

import os
from lib import db

COMMANDS = {'pwd', 'spwd', 'ls', 'sls', 'cd', 'scd', 'smkdir', 'srmdir'}

spath = '/'

def print_help():
    """Prints the navigation help prompts"""
    print "\n# Navigation:"
    print "  pwd               - get path of local directory"
    print "  spwd              - get path of stratus directory"
    print "  ls                - list files in local directory"
    print "  sls               - list files in stratus directory"
    print "  cd     [dir_path] - navigate to local directory at dir_path"
    print "  scd    [dir_path] - navigate to stratus directory at dir_path"
    print "  smkdir [dir_name] - create stratus directory at current path"
    print "  srmdir [dir_name] - remove stratus directory at current path"

def process_command(args):
    cmd = args[0]
    if cmd == 'pwd' and len(args) == 1:
        pwd()
    elif cmd == 'spwd' and len(args) == 1:
        spwd()
    elif cmd == 'ls' and len(args) == 1:
        ls()
    elif cmd == 'sls' and len(args) == 1:
        sls()
    elif cmd == 'cd' and len(args) == 2:
        cd(args[1])
    elif cmd == 'scd' and len(args) == 2:
        scd(args[1])
    elif cmd == 'smkdir' and len(args) == 2:
        smkdir(args[1])
    elif cmd == 'srmdir' and len(args) == 2:
        srmdir(args[1])
    else:
        print "Error: wrong number of arguments, please try again."

def pwd():
    """Prints the absolute path of the current local directory"""
    print os.getcwd()

def spwd():
    """Prints the absolute path of the current stratus directory"""
    print spath

def ls():
    """Lists all files and folders in the current local directory"""
    full = os.listdir(os.curdir)
    for f in full:
        if not f.startswith('.'):
            if os.path.isfile(f): print f
            elif os.path.isdir(f): print f + '/'

def sls():
    """Lists all files and folders in the current stratus directory"""
    db.listFiles(spath)

def cd(dir_path):
    """Move into the given local directory"""
    path = os.path.expanduser(dir_path)
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print "Error: '" + cd + "' is not a valid directory."

def scd(dir_name):
    """Move into the given stratus directory from the current path"""

def smkdir(dir_name):
    """Create a stratus directory from the current path"""
    db.createDirectory(spath, dir_name)

def srmdir(dir_name):
    """Delete a stratus directory at the current path"""
    db.removeDirectory(spath, dir_name)