"""
Exercise3 part1
Author: Yaniv Elayev
"""


def pancake_sort(array):
    """
    The function sorts a list by the pancake sort algorithm.
    :param array: A list of numbers
    :return: A sorted list
    """
    for index in range(len(array)):
        max_value_index = array.index(max(array[:len(array) - index]))
        array = reverse_list(array, max_value_index)
        array = reverse_list(array, len(array) - index - 1)
    return array


def reverse_list(array, max_index):
    """
    The function reverses list from the start to the given index.
    The rest of the values will be in the previous order
    :param array: A list
    :param max_index: Integer. The function reverse the list from the start to this value
    :return: new List
    """
    new_array = reversed(array[:max_index + 1])
    array = list(new_array) + array[max_index + 1:]
    return array


def main():
    """
    Main function. Gets numbers from the user and calls the pancake_sort function.
    :return:
    """
    list_to_sort = []
    user_input = input("insert numbers. when you want to stop insert 'done': ")
    while not user_input == 'done':
        list_to_sort.append(int(user_input))
        user_input = input("insert numbers. when you want to stop insert 'done': ")
    sorted_list = pancake_sort(list_to_sort)
    print(f"your sorted list: {sorted_list}")


if __name__ == '__main__':
    main()
