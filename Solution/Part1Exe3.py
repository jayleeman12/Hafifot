"""Part 1 Exercise 3"""
from random import randint


def pancake_sort(arr):
    """A function that sorts an array of integers using the pancake sort recursively.
    Args:
         array arr: Array of integers.
    Returns:
         array arr: A Sorted array.
    """
    if is_sorted(arr):
        return arr

    index = max_index(arr)
    arr = flip(arr, index)
    return arr[:1] + pancake_sort(arr[1:])


def flip(arr, index):
    """A function flips the values of the array from the index to the end as a stack.
    Args:
         array arr: Array of integers.
         int index: An index to flip the stack from.
    Returns:
          arr: A flipped array.
    """
    arr1 = arr[:index]
    arr2 = arr[index:]
    arr2.reverse()
    arr = arr1 + arr2
    arr.reverse()
    return arr


def is_sorted(arr):
    """A function that checks if an array of integers is sorted recursively.
    Args:
         array arr: Array of integers.
    Returns:
          bool: True or False.
    """
    length = len(arr)
    if length <= 1:
        return True

    if arr[length - 1] > arr[length - 2]:
        return False

    return is_sorted(arr[:length - 1])


def max_index(arr):
    """A function that returns the maximum number index in the array.
    Args:
         array arr: Array of integers.
    Returns:
          int: The index of the maximum number.
    """
    max_num = 0
    index = None
    for i, value in enumerate(arr):
        if value >= max_num:
            max_num = value
            index = i

    return index


def main():
    """Main function for user input and print result."""
    arr = []
    for _ in range(10):
        arr.append(randint(0, 50))
    print("before: ", arr)
    arr = pancake_sort(arr)
    print("after: ", arr)


if __name__ == '__main__':
    main()
