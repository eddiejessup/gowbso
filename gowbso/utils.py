from os.path import dirname, basename, splitext
import sys


def make_module_path_importable(file_path):
    dir_name = dirname(file_path)
    sys.path.append(dir_name)


def file_path_to_module_name(file_path):
    return splitext(basename(file_path))[0]
