"""
Exercise4 part1
Author: Yaniv Elayev
"""


def remove_duplicates(string):
    """
    The function removes duplicates from string
    :param string: A string
    :return: new string without duplicates
    """
    for character in string:
        character_instances = string.count(character)
        if character_instances > 1:
            string = string.replace(character, "")
    return string


def main():
    string = input("enter your string: ")
    string = remove_duplicates(string)
    print(f"your string without duplicates: {string}")


if __name__ == '__main__':
    main()
