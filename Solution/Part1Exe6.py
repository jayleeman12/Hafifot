"""Part 1 Exercise 6"""


def max_occurred(init_str: str):
    """A function that returns the highest occurred character in a string.
    Args:
        init_str: A string.
    Returns:
          char: The highest occurred character.
    """
    temp_dict = {}
    max_num = 0
    index = None
    for char in init_str:
        # just playing with some try and except
        try:
            temp_dict[char] += 1
        except KeyError:
            temp_dict[char] = 0

    for char in temp_dict:
        if temp_dict[char] >= max_num:
            max_num = temp_dict[char]
            index = char

    return index


def main():
    """Main function for user input and print result."""
    init_str = input("Enter string: ")
    print(f'Most occurred character: {max_occurred(init_str)}')


if __name__ == '__main__':
    main()
