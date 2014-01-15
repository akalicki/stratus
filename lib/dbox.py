"""
    stratus // dbox.py
    Author: Alex Kalicki (https://github.com/akalicki)
"""

import os
import dropbox
import accounts, db, navigate

DROPBOX_URL = "http://dropbox.com"
ACCOUNT_BUFFER = 1024
COMMANDS = {'put', 'get', 'mv', 'link', 'rm'}

def print_help():
    """Prints the file help prompts"""
    print "\n# File Operations:"
    print "  put  [lpath] [spath] - upload file from lpath to spath"
    print "  get  [spath] [lpath] - download file at spath to lpath"
    print "  mv   [path1] [path2] - move stratus file from path1 to path2"
    print "  link [path]          - get web links to stratus file at given path"
    print "  rm   [path]          - delete stratus file at given path"

def process_command(args):
    cmd = args[0]
    if cmd == 'put' and len(args) == 3:
        put(args[1], args[2])
    elif cmd == 'get' and len(args) == 3:
        get(args[1], args[2])
    elif cmd == 'mv' and len(args) == 3:
        mv(args[1], args[2])
    elif cmd == 'link' and len(args) == 2:
        link(args[1])
    elif cmd == 'rm' and len(args) == 2:
        rm(args[1])
    else:
        print "Error: wrong number of arguments, please try again."

def put(lpath, spath):
    """Uploads file from lpath to spath"""
    abs_path = navigate.get_abs_path(spath)
    parent, name = navigate.split_path(abs_path)
    up_parent, up_name = navigate.split_path(parent)
    file_size = os.stat(lpath).st_size
    if up_parent is not None and not db.directory_exists(up_parent, up_name):
        print "Error: '" + parent + "' is not a valid directory."
    elif db.file_exists(parent, name):
        print "Error: '" + spath + "' already exists."
    elif file_size > 2 * 1024 * 1024 * 1024 - ACCOUNT_BUFFER:
        print "Error: individual files must be 2GB or smaller."
    else:   
        access_token = accounts.get_useable_account(file_size)
        client = dropbox.client.DropboxClient(access_token)
        lfile = open(lpath)
        client.put_file('/' + name, lfile)
        db.add_file(access_token, parent, name)
        lfile.close()

def get(spath, lpath):
    """Downloads file at spath to lpath"""

def mv(old_path, new_path):
    """Moves stratus file from old_path to new_path"""

def link(path):
    """Prints web links to stratus file at given path"""
    abs_path = navigate.get_abs_path(path)
    parent, name = navigate.split_path(abs_path)
    access_token = db.get_access_to_file(parent, name)
    if access_token is not None:
        dbox_path = '/' + name
        client = dropbox.client.DropboxClient(access_token)
        short_link = client.share(dbox_path)['url']
        normal_link = client.share(dbox_path, short_url=False)['url']
        dl_link = normal_link.replace('www.dropbox.com',
                                      'dl.dropboxusercontent.com', 1)
        print "short link:     " + short_link
        print "normal link:    " + normal_link
        print "download link:  " + dl_link

def rm(path):
    """Deletes stratus file at given path"""
    abs_path = navigate.get_abs_path(path)
    parent, name = navigate.split_path(abs_path)
    access_token = db.get_access_to_file(parent, name)
    if access_token is not None:
        dbox_path = '/' + name
        client = dropbox.client.DropboxClient(access_token)
        client.file_delete(dbox_path)
        db.remove_file(access_token, parent, name)

def account_space(access_token):
    """Gets amount of free space in the given account"""
    client = dropbox.client.DropboxClient(access_token)
    account_info = client.account_info()
    quota_info = account_info['quota_info']
    total = quota_info['quota']
    used = quota_info['normal'] + quota_info['shared']
    return total - used