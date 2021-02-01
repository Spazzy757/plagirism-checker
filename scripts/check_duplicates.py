"""
This script takes a hash file and checks it against
the redis instance for duplication
"""

import redis
import os

from os import listdir
from os.path import isfile, join


REDIS_HOST = os.getenv("REDIS_HOST", "")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
HASH_FILE_NAME = os.getenv("HASH_FILE_NAME", "")


def check_duplicates():
    """
    Takes a Hash File and iterates through iut checking for duplicates
    """
    count = 0
    duplicate_count = 0
    r = redis.Redis(host=REDIS_PORT, port=REDIS_PORT, db=REDIS_DB)
    file1 = open(HASH_FILE_NAME, 'rb')
    lines = file1.readlines()
    for line in lines:
        if res:
            res = r.get(line.strip())
             duplicate_count += int(res)
        count += 1
    return  duplicate_count/count*100


if __name__ == "__main__":
    unique_score = check_duplicates()
    print(f"Unique Score: {unique_score}")
