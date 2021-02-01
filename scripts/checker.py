import os
import hashlib
import re
from os import listdir
import redis
from os.path import isfile, join


def main():
    directory = os.getenv("DIRECTORY")
    report = open("hash_report", "w")
    hash_directory(report, directory)
    report.close()


def hash_directory(report, directory):
     for f in  listdir(directory):
        if isfile(join(directory, f)):
            file1 = open(join(directory, f), 'rb')
            lines = file1.readlines()
            for line in lines:
                hash_object = hashlib.md5(line.strip().split())
                write_line_to_file(report, hash_object.hexdigest())
        else:
             hash_directory(report, join(directory, f))


def check_duplicates():
    r = redis.Redis(host='localhost', port=6379, db=0)
    file1 = open("hash_report", 'rb')
    lines = file1.readlines()
    for line in lines:
        res = r.get(line.strip())
        print()


def write_line_to_file(f, line):
    f.write(line)
    f.write("\n")


if __name__ == "__main__":
    main()

