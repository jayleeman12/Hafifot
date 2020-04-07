"""Part 1 Exercise 5"""


def permutation(arr: list, start_index: int):
    """A function that prints all the permutations of the set {1...n} recursively.
    Args:
        arr: The set to work on.
        start_index: The index in the original set to start permutation from
    """
    if start_index == len(arr)-1:
        print(''.join(arr))

    for i in range(start_index, len(arr)):
        arr[start_index], arr[i] = arr[i], arr[start_index]
        permutation(arr, start_index + 1)
        arr[start_index], arr[i] = arr[i], arr[start_index]


def main():
    """Main function for user input and print result."""
    arr = input("Enter string: ")
    permutation(list(arr), 0)


if __name__ == '__main__':
    main()
