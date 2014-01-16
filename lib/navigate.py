"""
    stratus // navigate.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

import os
import db

COMMANDS = {'pwd', 'lpwd', 'ls', 'lls', 'cd', 'lcd', 'mkdir', 'rmdir'}
spath = ''

def print_help():
    """Prints the navigation help prompts"""
    print "\n# Navigation:"
    print "  pwd          - get path of stratus directory"
    print "  lpwd         - get path of local directory"
    print "  ls           - list files in stratus directory"
    print "  lls          - list files in local directory"
    print "  cd    [path] - navigate to stratus directory at path"
    print "  lcd   [path] - navigate to local directory at path"
    print "  mkdir [path] - create stratus directory at given path"
    print "  rmdir [path] - remove stratus directory at given path"

def process_command(args):
    cmd = args[0]
    if cmd == 'pwd' and len(args) == 1:
        pwd()
    elif cmd == 'lpwd' and len(args) == 1:
        lpwd()
    elif cmd == 'ls' and len(args) == 1:
        ls()
    elif cmd == 'lls' and len(args) == 1:
        lls()
    elif cmd == 'cd' and len(args) == 2:
        cd(args[1])
    elif cmd == 'lcd' and len(args) == 2:
        lcd(args[1])
    elif cmd == 'mkdir' and len(args) == 2:
        mkdir(args[1])
    elif cmd == 'rmdir' and len(args) == 2:
        rmdir(args[1])
    else:
        print "Error: wrong number of arguments, please try again."

def pwd():
    """Prints the absolute path of the current stratus directory"""
    print '/' + spath

def lpwd():
    """Prints the absolute path of the current local directory"""
    print os.getcwd()

def ls():
    """Lists all files and folders in the current stratus directory"""
    db.list_files(spath)

def lls():
    """Lists all files and folders in the current local directory"""
    full = os.listdir(os.curdir)
    for f in full:
        if not f.startswith('.'):
            if os.path.isfile(f): print f
            elif os.path.isdir(f): print f + '/'

def cd(path):
    """Moves into the given stratus directory"""
    abs_path = get_abs_path(path)
    parent, name = split_path(abs_path)
    if parent is None or db.directory_exists(parent, name):
        global spath
        spath = abs_path
    else:
        print "Error: '" + abs_path + "' is not a valid directory."

def lcd(path):
    """Moves into the given local directory"""
    path = os.path.expanduser(path)
    if os.path.isdir(path):
        os.chdir(path)
    else:
        print "Error: '" + path + "' is not a valid directory."

def mkdir(path):
    """Creates a stratus directory at the given path"""
    abs_path = get_abs_path(path)
    parent, name = split_path(abs_path)
    db.create_directory(parent, name)

def rmdir(path):
    """Deletes a stratus directory at the given path"""
    abs_path = get_abs_path(path)
    parent, name = split_path(abs_path)
    db.remove_directory(parent, name)
    if abs_path == spath:
        global spath
        spath = get_abs_path('..')

def get_abs_path(path):
    """Resolves path into a clean, usable absolute stratus path"""
    if path == '.':
        return spath
    abs_path = spath
    if path.startswith('/') or abs_path == '':
        abs_path = path
    else:
        if path.startswith('./'):
            path = path[2:]
        while path.startswith('..'):
            path = path.lstrip('..')
            path = path.lstrip('/')
            if abs_path.count('/') == 0:
                abs_path = ''
            else:
                abs_path = abs_path.rsplit('/', 1)[0]
        abs_path = abs_path + '/' + path
    abs_path = abs_path.strip('/')
    return abs_path

def split_path(abs_path):
    """Gets the parent and name of the directory at the given path"""
    if abs_path == '': # root folder
        return [None, '']
    elif abs_path.count('/') == 0: # inside root
        return ['', abs_path]
    return abs_path.rsplit('/', 1)