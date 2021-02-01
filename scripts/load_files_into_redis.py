"""
This script is used to populate a redis instance with previous hash files
"""

import redis
import os

from os import listdir
from os.path import isfile, join


REDIS_HOST = os.getenv("REDIS_HOST", "")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
LOAD_DIRECTORY = os.getenv("LOAD_DIRECTORY", "")


def load_files_into_redis():
    """
    Takes a Directory Of Hash Files and Loads Them Into a Redis Instance
    """
    r = redis.Redis(host=REDIS_PORT, port=REDIS_PORT, db=REDIS_DB)
    for f in listdir(LOAD_DIRECTORY):
        if isfile(join(directory, f)):
            file1 = open(join(directory, f), 'rb')
            lines = file1.readlines()
            for line in lines:
                res = r.set(line.strip(), 1)


if __name__ == "__main__":
    load_files_into_redis()
