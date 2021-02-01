# Plagirism Checker

Really simple implementation of comparing two or more code directories

The idea is based around converting a directory of files into a single hash report, this hash report
can then be loaded into a redis instance and each hash report can be checked against the redis instance for the uniqueness


**Note** This is not a fool proof solution and there are ways around it if the submissions is knows how the check is implemented

## Hash Directory

Takes a directory and generates a "Hash Report" of that directory in order to be used later. This will essentially be a list of hashed lines found in the directory

``` bash
export TEST_DIRECTORY='codebase/'
export REPORT_NAME='code_base_hash_report'

python scripts/hash_directory.py
```

## Load Hash Reports Into Redis

As you generate more reports you can load them into redis by collecting them in a directory and running the following:

``` bash
export REDIS_HOST='localhost'
export REDIS_PORT='6379'
export REDIS_DB='0'
export LOAD_DIRECTORY='hash_reports/'

python scripts/load_files_into_redis.py
```

## Check for uniqueness

Once you have a couple of hash reports you can start checking the uniqueness of submissions by running a check against the redis instance

``` bash
export REDIS_HOST='localhost'
export REDIS_PORT='6379'
export REDIS_DB='0'
export HASH_FILE_NAME='code_base_hash_report'

python scripts/check_duplicates.py
```

