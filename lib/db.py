"""
    stratus // db.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

from navigate import split_path
from pymongo import MongoClient

client = MongoClient()
db = client.stratus

def directory_exists(parent, name):
    """Returns whether the given directory already exists"""
    return db.dirs.find({'parent': parent, 'name': name}).count() > 0

def directory_empty(parent, name):
    """Returns whether the given directory is empty"""
    if parent == '':
        abs_path = name
    else:
        abs_path = parent + '/' + name
    return db.dirs.find({'parent': abs_path}).count() == 0

def create_directory(parent, name):
    """creates stratus directory with given name at the current path"""
    up_parent, up_name = split_path(parent)
    if up_parent is not None and not directory_exists(up_parent, up_name):
        print "Error: '" + up_name + "' is not a valid directory."""
    elif directory_exists(parent, name):
        print "Error: '" + name + "' already exists."
    else:
        new_dir = {'parent': parent, 'name': name}
        db.dirs.insert(new_dir)

def remove_directory(parent, name):
    """deletes stratus directory with given name at the current path"""
    if not directory_exists(parent, name):
        print "Error: '" + name + "' is not a valid directory."
    elif not directory_empty(parent, name):
        print "Error: '" + name + "' is not empty."
    else:
        db.dirs.remove({'parent': parent, 'name': name})

def list_files(path):
    dirs = db.dirs.find({'parent': path}, {'name': 1, '_id': 0})
    for directory in dirs:
        print directory['name'] + "/"