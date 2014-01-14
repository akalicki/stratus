"""
    stratus // db.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

import pymongo
import dbox
import navigate

client = pymongo.MongoClient()
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
    """Creates stratus directory with given name at the current path"""
    up_parent, up_name = navigate.split_path(parent)
    if up_parent is not None and not directory_exists(up_parent, up_name):
        print "Error: '" + up_name + "' is not a valid directory."""
    elif directory_exists(parent, name):
        print "Error: '" + name + "' already exists."
    else:
        new_dir = {'parent': parent, 'name': name}
        db.dirs.insert(new_dir)

def remove_directory(parent, name):
    """Deletes stratus directory with given name at the current path"""
    if not directory_exists(parent, name):
        print "Error: '" + name + "' is not a valid directory."
    elif not directory_empty(parent, name):
        print "Error: '" + name + "' is not empty."
    else:
        db.dirs.remove({'parent': parent, 'name': name})

def list_files(path):
    """Lists all folders and files in current stratus directory"""
    dirs = db.dirs.find({'parent': path}, {'name': 1, '_id': 0})
    for directory in dirs:
        print directory['name'] + "/"

def add_account(dbox_id, access_token):
    """Adds Dropbox account info to the database for future use"""
    available_space = dbox.account_space(access_token)
    new_account = {'dbox_id': dbox_id,
                   'access_token': access_token,
                   'available_space': available_space}
    db.accounts.insert(new_account)