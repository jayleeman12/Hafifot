"""Part 1 Exercise 4"""


def remove_duplicates(init_str):
    """A function that removes duplicate characters from a string.
    Args:
        init_str: A string.
    Returns:
          clean_str: The string without the duplicates.
    """
    temp_dict = {}
    clean_str = ""
    for char in init_str:
        temp_dict[char] = char

    for char in temp_dict:
        clean_str += temp_dict[char]

    return clean_str


def main():
    """Main function for user input and print result."""
    init_str = input("Enter string: ")
    print("The result is: ", remove_duplicates(init_str))


if __name__ == '__main__':
    main()
