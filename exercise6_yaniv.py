"""
Exercise6 part1
Author: Yaniv Elayev
"""


def get_highest_occurred_character(string):
    """
    The function returns the highest occurred character in a string
    :param string: A string
    :return: string.
    """
    highest_instances_number = 0
    highest_occurred_character = ""
    for character in string:
        current_character_instances = string.count(character)
        if current_character_instances > highest_instances_number:
            highest_occurred_character = character
            highest_instances_number = current_character_instances
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
