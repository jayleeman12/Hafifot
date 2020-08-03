"""
Exercise6 part1
Author: Yaniv Elayev
"""


def get_highest_occurred_character(string):
    """
    The function returns the highest occurred character in a string.
    This function does not use string.count, so the Complexity is o(n).
    :param string: A string
    :return: string.
    """
    characters_dictionary = {}
    for character in string:
        characters_dictionary[character] = 0
    for character in string:
        characters_dictionary[character] += 1
    highest_instances_number = 0
    highest_occurred_character = ""
    for character in string:
        if characters_dictionary[character] > highest_instances_number:
            highest_occurred_character = character
            highest_instances_number = characters_dictionary[character]
    return highest_occurred_character


def main():
    """
    Main function. Gets input from user and prints the highest occurred character.
    :return:
    """
    user_input = input("insert your string: ")
    highest_occurred_character = get_highest_occurred_character(user_input)
    print(f"the highest occurred character is: {highest_occurred_character}")


if __name__ == '__main__':
    main()
