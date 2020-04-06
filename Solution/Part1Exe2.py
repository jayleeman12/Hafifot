"""Part 1 Exercise 2"""


def anagram(str1, str2):
    """A function that checks if two strings are anagrams of each other recursively.
    Args:
        str str1: first string.
        str str2: second string.
    Returns:
          True or False.
    """
    if len(str1) != len(str2):
        return False

    if str1 == str2:
        return True

    for i, char in enumerate(str2):
        if str1[0] == char:
            return anagram(str1[1:], str2[:i] + str2[i+1:])

    return False


def main():
    """Main function for user input and print result."""
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print("The result is: ", anagram(''.join(filter(str.isalpha, str1)).lower(),
                                     ''.join(filter(str.isalpha, str2)).lower()))


if __name__ == '__main__':
    main()
