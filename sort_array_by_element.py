def frequency_sort(items):
    # form dictionary from list with elements as keys and values as occurencies
    di_items = dict()
    for i in items:
      di_items[i] = di_items.get(i, 0) + 1
    # sort our dictionary by occurency
    sorted_by_value = dict(sorted(di_items.items(), key=lambda kv: kv[1], reverse=True))
    # create nes list from sorted by occurency dictionary
    result_list = list()
    for k in sorted_by_value:
      for r in range(sorted_by_value[k]):
        result_list.append(k)
    return result_list


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")