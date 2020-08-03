"""
Exercise2 part1
Author: Yaniv Elayev
"""


def is_anagram(first_string, second_string):
    """
    The functions checks if two strings are anagrams of each other
    :param first_string: First string
    :param second_string: Second string
    :return: True if the strings are anagrams of each other, else False
    """
    characters_dictionary = {}
    for character in first_string:
        characters_dictionary[character] = 0
    for character in first_string:
        characters_dictionary[character] += 1
    for character in second_string:
        if characters_dictionary.get(character, -1) == -1:
            return False
        else:
            characters_dictionary[character] -= 1
    for character in first_string:
        if not characters_dictionary[character] == 0:
            return False
    return True


def main():
    """
    Main Function. Gets input from the user and calls the is_anagram function
    :return:
    """
    first_string = input("insert your first string: ")
    second_string = input("insert your second string: ")
    if is_anagram(first_string, second_string):
        print("your strings are anagrams of each other")
    else:
        print("your string are not anagrams of each other")


if __name__ == '__main__':
    main()
