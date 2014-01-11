"""
    stratus // db.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

from pymongo import MongoClient

client = MongoClient()
db = client.stratus

def directoryExists(parent, name):
    """returns whether the given d irectory already exists"""
    return db.dirs.find({'parent': parent, 'name': name}).count() > 0

def createDirectory(parent, name):
    """creates stratus directory with given name at the current path"""
    if directoryExists(parent, name):
        print "Error: '" + name + "' already exists."
    else:
        new_dir = {'parent': parent, 'name': name}
        db.dirs.insert(new_dir)

def removeDirectory(parent, name):
    """deletes stratus directory with given name at the current path"""
    if directoryExists(parent, name):
        db.dirs.remove({'parent': parent, 'name': name})
    else:
        print "Error: '" + name + "' is not a valid directory."

def listFiles(path):
    dirs = db.dirs.find({'parent': path}, {'name': 1, '_id': 0})
    for directory in dirs:
        print directory['name'] + "/"