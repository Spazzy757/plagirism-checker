"""
This script generates a hash file of all the files in a directory
so as to be able to check it later
"""
import os
import hashlib
import re
from os import listdir

from os.path import isfile, join


TEST_DIRECTORY =  os.getenv("DIRECTORY")
REPORT_NAME = os.getenv("REPORT_NAME")

def hash_directory():
    """
    Takes in a directory and starts the report creation process
    """
    report = open(REPORT_NAME, "w")
    calculate_hash_file(report, TEST_DIRECTORY)
    report.close()


def calculate_hash_file(report, directory):
    """
    Recursively goes through files in a directory and
    generates a hash for every line of every file
    """
    for fi in  listdir(directory):
        if isfile(join(directory, fi)):
            f = open(join(directory, fi), 'rb')
            lines = f.readlines()
            for line in lines:
                hash_object = hashlib.md5(line.strip())
                write_line_to_file(report, hash_object.hexdigest())
            f.close()
        else:
            calculate_hash_file(report, join(directory, fi))

def write_line_to_file(f, line):
    """
    Writes a new line to a file
    """
    f.write(line)
    f.write("\n")


if __name__ == "__main__":
    hash_directory()
