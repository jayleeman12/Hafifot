"""Part 2 Exercise 1"""
from Hafifot.Solution.packages.file_store_module import *


def main():
    """Main function"""

    # Create a file store from type OS instance
    file_store_type = input('choose file_store: OS/ObjectStorage/Proxy: ')
    file_store_path = input('Enter file store path: ')
    file_factory = OSFileStore(file_store_path)


if __name__ == '__main__':
    main()
