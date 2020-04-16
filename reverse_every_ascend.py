def reverse_ascending(items):
    """
    This function makes reverse sorting if list inside every maximal strictly ascending sublist.
    :param items: list of integers as only parameter
    :return: a new list that contains the same elements as the argument iterable items, but with the reversed
    order of the elements inside every maximal strictly ascending sublist.
    """
    # function returns empty list in case if original list has no elements in it
    if len(items) == 0:
        return []
    # if original list has elements inside function loops through the list and compares each element with preceding
    else:
        # loops starts from 1 element in list and compares it with preceding element
        for i in range(1, len(items)):
            # if preceding element is greater than current item,
            # than preceding element is ending of inside ascending sublist, and function makes recursive call
            if items[i] <= items[i-1]:
                # function returns sorted in ascending order inside ascending sublist and calls itself,
                # passing as its only parameter all items starting from current 'i' element
                return sorted(items[:i], reverse=True) + reverse_ascending(items[i:])
        # otherwise, function finishes loop through the list, meaning that all items in the list or in
        # sublist are in ascending order. In such case function returns reverse sorted list or sublist
        return sorted(items, reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")