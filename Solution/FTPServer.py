"""Part 2 Exercise 1"""
import os
from typing import List


def store_file(file_to_store: object):
    """A function that get a file object and write it to a new file in the server"""
    with open(f'files/{file_to_store.name}', 'w') as saved_file:
        for line in file_to_store:
            saved_file.write(line)


def get_all_files() -> List:
    """A function that returns a list of all the files in the server"""
    all_files = []
    for file in os.listdir("files/"):
        with open(file, 'r') as returned_file:
            all_files.append(returned_file)

    return all_files


def get_file(file_name: str) -> object:
    """A functions that gets a file name and returns the file from the server (if exist, else returns None)"""
    for file in os.listdir("files/"):
        if file == file_name:
            with open(file, 'r') as returned_file:
                return returned_file

    return None


def main():
    """Main function"""


if __name__ == '__main__':
    main()
