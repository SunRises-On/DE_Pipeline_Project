import os


def get_file_path(fn):
    current_directory = os.path.dirname(__file__)
    current_directory = os.path.split(current_directory)
    parent_directory = current_directory[0]
    parent_directory = return_parent_dir(parent_directory, 3)
    file_path = join_file_path(parent_directory,fn)
    return file_path


def return_parent_dir(parent_directory, x):
    
    for x in range(x):

        parent_directory = os.path.split(parent_directory)
        parent_directory = parent_directory[0]

    return parent_directory



def join_file_path(parent_directory, fn):
    file_path = os.path.join(parent_directory,fn)
    return file_path