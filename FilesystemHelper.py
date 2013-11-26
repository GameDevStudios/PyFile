#!/usr/bin/env python


from OsHelper import Os
from os.path import expanduser


import os


class Filesystem():

    '''

    A simple helper module for making folders and files.

    '''

    def __init__(self, default_dir=expanduser('~')):
        '''

        Creates a new Filesystem object.


        Takes 1 argument:

        default_dir - The default directory to start in. Set to the users home directory if no value is provided.

        '''

        self.os_instance = Os()

        self.os = self.os_instance.get_os()

        self.homedir = expanduser('~')

        if default_dir is None:
            default_dir = expanduser('~')

        self.working_dir = default_dir

    def get_home_dir(self):
        '''

        Returns your home directory.

        '''

        return self.homedir

    def file_exists(self, file_name):
        '''

        Checks if a file exists. Returns True if a file exists, false otherwise.

        Takes 1 argument:

        file_name - The name of the file to check.

        '''

        return True if os.path.exists(file_name) else False

    def pwd(self):
        '''

        Returns the users current working directory. 

        '''

        return self.working_dir

    def get_dir_items(self, directory=None):
        '''

        Returns list of items in a directory, showing hidden folders.

        Takes 1 argument:

        directory - The directory from which to get the directory items. If no directory is provided it is set to the users current working directory.

        '''

        item_list = []

        if directory is None:
            directory = self.pwd()

        for item in os.listdir(directory):
            item_list.append(item)

        return item_list

    def change_directory(self, directory=None, pathtype='absolute'):
        '''

        Changes the users directory. Returns the new directory.

        Takes 2 arguments:

        directory - The directory to change to.
        pathtype - The type of path. Can be either 'absolute' or 'relative'. 'abs' and 'rel' work too.

        '''

        if directory is None:
            directory = self.working_dir

        if pathtype.startswith('abs'):
            os.chdir(directory)
        elif pathtype.startswith('rel'):
            os.chdir(os.path.join(self.working_dir, directory))

        self.working_dir = os.getcwd()

        return self.working_dir

    def make_dir(self, folder_name, folder_path=None, pathtype='abs'):
        '''

        Creates a directory. Returns True if the directory already exists, returns the directory otherwise.

        Takes 3 arguments:

        folder_name - The name of the directory that you wish to create. Value must be provided.
        folder_path - The path to the directory that you wish to create. If no value is provided it is defaulted to the current working directory.
        pathtype - The type of path. Can be either 'abs' or 'rel'. If no value is provided it is defaulted to 'abs'.

        '''

        if folder_path is None:
            folder_path = self.working_dir

        if folder_name is None:
            print "Sorry! A value must be provided for a directory name.\n\n"

        if pathtype is 'abs':
            if os.path.exists(os.path.join(folder_path, folder_name)):
                return True
            elif not os.path.exists(os.path.join(folder_path, folder_name)):
                os.makedirs(os.path.join(folder_path, folder_name))

                return folder_path
        elif pathtype is 'rel':
            if os.path.exists(os.path.join(self.working_dir, folder_name)):
                return True
            elif not os.path.exists(os.path.join(self.working_dir, folder_path)):
                os.makedirs(os.path.join(self.working_dir, folder_path))

                return str(os.path.join(self.working_dir, folder_path))
