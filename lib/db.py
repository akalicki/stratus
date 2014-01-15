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
    """Creates stratus directory with given name in the parent folder"""
    up_parent, up_name = navigate.split_path(parent)
    if up_parent is not None and not directory_exists(up_parent, up_name):
        print "Error: '" + up_name + "' is not a valid directory."
    elif directory_exists(parent, name):
        print "Error: '" + name + "' already exists."
    else:
        new_dir = {'parent': parent, 'name': name}
        db.dirs.insert(new_dir)

def remove_directory(parent, name):
    """Deletes stratus directory with given name in the parent folder"""
    if not directory_exists(parent, name):
        print "Error: '" + name + "' is not a valid directory."
    elif not directory_empty(parent, name):
        print "Error: '" + name + "' is not empty."
    else:
        db.dirs.remove({'parent': parent, 'name': name})

def list_files(path):
    """Lists all folders and files in given stratus directory"""
    dirs = db.dirs.find({'parent': path})
    for d in dirs:
        print d['name'] + "/"
    files = db.files.find({'parent': path})
    for f in files:
        print f['name']

def add_account(access_token):
    """Adds Dropbox account info to the database for future use"""
    available_space = dbox.account_space(access_token)
    new_account = {'access_token': access_token,
                   'available_space': available_space}
    db.accounts.insert(new_account)

def find_account_with_space(space):
    """Returns account with free space or None if not found"""
    needed_space = space - dbox.ACCOUNT_BUFFER
    return db.accounts.find_one({'available_space': {'$gte': needed_space}})

def add_file(access_token, parent, name):
    """Adds file info to the database for future use"""
    new_file = {'access_token': access_token, 'parent': parent, 'name': name}
    db.files.insert(new_file)
    updated_space = dbox.account_space(access_token)
    db.accounts.update({'access_token': access_token},
                       {'$set': {'available_space': updated_space}})
