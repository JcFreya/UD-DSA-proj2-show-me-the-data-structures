"""
# Problem 2: File Recursion
write code for finding all files under a directory (and all directories beneath it) that end with ".c"
"""

import os

def find_files(suffix, path=None):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_list = []

    # check if path is None
    if path is None:
        print("Erro: Path couldn't be None")
        return -1

    # check if path exists
    if not os.path.exists(path):
        print("Erro: Path not exists")
        return -1

    # check if the path is a file
    if os.path.isfile(path):
        # check if the file end with suffix
        if path.endswith(suffix):
            return [path]
    else:
        # get file list in the directory and check suffix
        sub_paths = os.listdir(path)
        for file in sub_paths:
            path_list += find_files(suffix,  "{}/{}".format(path, file))

    return path_list


print('----------Test1----------')
# find all files under current directory that ends with '.c'
print(find_files('.c', '.'))
# ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c']
print('\n')

print('----------Test2----------')
# find all files in the path
print(find_files('', './testdir'))  # all files in the path
# ['./testdir/subdir4/.gitkeep', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir3/subsubdir1/b.c',
# './testdir/t1.c', './testdir/subdir2/.gitkeep', './testdir/subdir5/a.h', './testdir/subdir5/a.c',
# './testdir/t1.h', './testdir/subdir1/a.h', './testdir/subdir1/a.c']
print('\n')

print('----------Test3----------')
# find all files under current directory that ends with '.h'
print(find_files('.h', '.'))
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
print('\n')

print('----------Test4----------')
# test invalid input path
print(find_files('.h'))     # -1, Erro: Path couldn't be None
print('\n')

print('----------Test5----------')
# test invalid input path
print(find_files('.h', './test')) # -1, Erro: Path not exists
print('\n')
