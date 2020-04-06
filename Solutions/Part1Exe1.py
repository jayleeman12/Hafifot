def factorial(number):
    """Calculate the factorial of a number recursively.

    Args:
        int number: the number to calculate its factorial.

    Returns:
          The result of the calculation.
    """
    if number == 1:
        return 1
    return number * factorial(number - 1)


def main():
    """Main function for user input and print result."""
    number = input("Enter your number: ")
    print("Factorial is: ", factorial(int(number)))


if __name__ == '__main__':
    main()