#!/usr/bin/env python


from OsHelper import Os
from os.path import expanduser


import os
import shutil


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
            return

        if pathtype.startswith('abs'):
            if os.path.exists(os.path.join(folder_path, folder_name)):
                return True
            elif not os.path.exists(os.path.join(folder_path, folder_name)):
                os.makedirs(os.path.join(folder_path, folder_name))

                return folder_path
        elif pathtype.startswith('rel'):
            if os.path.exists(os.path.join(self.working_dir, folder_name)):
                return True
            elif not os.path.exists(os.path.join(self.working_dir, os.path.join(folder_path, folder_name))):
                os.makedirs(
                    os.path.join(self.working_dir, os.path.join(folder_path, folder_name)))

                return os.path.join(self.working_dir, folder_path)

    def remove_dir(self, folder_name, folder_path=None, pathtype='abs'):
        '''

        Removes a specified folder at a specified directory. Note that this also removes all subdirectories and files in that directory. Returns True if the file is successfully removed, False otherwise.

        Takes 3 arguments:

        folder_name - Name of the folder that you wish to remove. This value cannot be blank.
        folder_path - Path to the folder that you wish to remove. If no value is passed this is defaulted to the current working directory.
        pathtype - The type of path. This can either be 'abs' or 'rel'.

        '''

        if folder_path is None:
            folder_path = self.working_dir

        if folder_name is None:
            print "Sorry! A value must be provided for a directory name.\n\n"

            return

        if pathtype.startswith('abs'):
            if os.path.exists(os.path.join(folder_path, folder_name)):
                shutil.rmtree(os.path.join(folder_path, folder_name))
            elif not os.path.exists(os.path.join(folder_path, folder_name)):
                return False
        elif pathtype.startswith('rel'):
            if os.path.exists(os.path.join(self.working_dir, folder_name)):
                shutil.rmtree(os.path.join(self.working_dir, folder_name))
            elif not os.path.exists(os.path.join(self.working_dir, folder_name)):
                return False

    def dir_exists(self, folder_name, folder_path=None, pathtype='abs'):
        '''

        Checks if a file exists. Returns True if the directory name specified at the directory path exists, False otherwise.


        Takes 3 arguments:

        folder_name - The name of the folder. This cannot be blank.
        folder_path - The path to the folder. If left blank this is defaulted to the current working directory.
        pathtype - The type of path. This can be 'abs' or 'rel'.

        '''

        if folder_path is None:
            folder_path = self.working_dir

        if folder_name is None:
            print "Sorry! A value must be provided for a directory name.\n\n"

            return

        if pathtype.startswith('abs'):
            if os.path.exists(os.path.join(folder_path, folder_name)):
                return True
            elif not os.path.exists(os.path.join(folder_path, folder_name)):
                return False
        elif pathtype.startswith('rel'):
            if os.path.exists(os.path.join(self.working_dir, folder_name)):
                return True
            elif not os.path.join(os.path.join(self.working_dir, folder_name)):
                return False

    def make_file(self, file_name, file_path, pathtype='abs', filemode='r+'):
        '''

        Creates a new file with the specified name and path. Returns file if the file can be created, False otherwise.


        Takes 4 arguments:

        file_name - Name of the file to create. This cannot be blank.
        file_path - Path to the file to create. If left blank it is defaulted to the current working directory.
        pathtype - Type of path. Can be either 'abs' or 'rel'.
        filemode - Mode to open the file.

        '''

        if file_name is None:
            print "Sorry! A value must be provided for a file name.\n\n"

            return

        if file_path is None:
            file_path = self.working_dir

        if pathtype.startswith('abs'):
            f = open(os.path.join(file_path, file_name), filemode)

            return f
        elif pathtype.startswith('rel'):
            f = open(os.path.join(file_path, file_name), filemode)

            return f

    def read_file(self, file_name, file_object=None, file_path=None, pathtype='abs'):
        '''

        Reads a file. Returns contents of the file, False otherwise.


        Takes 4 arguments:

        file_name - Name of the file to read from. This feild is required.
        file_object - File object to read from. If blank this is defaulted to None, and instead creates a file based on the information provided (filename and filepath)
        file_path - Path to the file to create. If blank this is defaulted to the current working directory.
        pathtype - Type of path. Can be 'abs' or 'rel'.

        '''

        if file_name is None and file_object is None:
            print "Sorry! A value must be provided.\n\n"

            return

        if file_name is None:
            print "Sorry! A value must be provided."

            return

        if file_path is None:
            file_path = self.working_dir

        if file_object is None:
            if pathtype.startswith('abs'):
                f = open(os.path.join(file_path, file_name), 'r')

                print type(f)

                return f.read()
            elif pathtype.startswith('rel'):
                f = open(os.path.join(self.working_dir, filename), 'r')

                return f.read()
        elif file_object is not None:
            return file_object.read()

    def write_file(self, file_name, file_object=None, file_path=None, pathtype='abs', text_to_write='Hello World'):
        '''

        Writes to a file. Returns True if file is successfully written to, False otherwise.


        Takes 5 arguments:

        file_name - The name of the file to write to. A value must be provided for this.
        file_object - An optional parameter that is a file object to write to. A value is not needed if a value is provided for file_name.
        file_path - Path to the file to write to. If blank it is defaulted to the current working directory.
        pathtype - Type of path. Can be 'abs' or 'rel'.
        text_to_write - Text to write to file. If blank is defaulted to 'Hello World!'.

        '''

        if file_name is None and file_object is None:
            print "Sorry! A value must be provided.\n\n"

            return

        if file_name is None:
            print "Sorry! A value must be provided.\n\n"

        if file_path is None:
            file_path = self.working_dir

        if file_object is None:
            if pathtype.startswith('abs'):
                f = open(os.path.join(file_path, file_name), 'w')

                f.write(text_to_write)

                return True
            elif pathtype.startswith('rel'):
                f = open(os.path.join(file_path, file_name), 'r')

                f.write(text_to_write)

                return True
            else:
                return False
        elif file_object is not None:
            file_object.write(text_to_write)

            return True

    def change_file_mode(self, file_object, filemode):
        '''
        Recreates the file by closing the file_object passed in and opening it again with the new file mode. Returns the new file object.


        Takes 2 arguments:

        file_object - The file object you wish to change the mode of. Cannot be left blank.
        filemode - The new mode to change the file to. Cannot be left blank.

        '''

        if file_object is None:
            print "Sorry! A value must be provided."

            return

        if filemode is None:
            print "Sorry! A value must be provided."

            return

        file_object.close()

        f = open(file_object.name, filemode)

        return f
