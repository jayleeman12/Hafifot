"""
Exercise1 part1
Author: Yaniv Elayev
"""


def factorial(number):
    """
    The function calculates the factorial of a number
    :param number:  An integer
    :return: The factorial of the given number
    """
    if number == 1:
        return number
    return number * factorial(number - 1)


def main():
    """
    Main function. Calls the factorial function
    :return:
    """
    number = input("insert your number: ")
    print(f"The factorial of your number is {factorial(int(number))}")


if __name__ == '__main__':
    main()
