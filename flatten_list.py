def flat_list(array):
    import re
    # convert our list to string to apply re module
    str_array = str(array)
    # using re.findall() searching for all positive and negative numbers
    searched_text = re.findall(r'[+-]?\d+', str_array)
    print(searched_text)
    li = []
    # convert our list with string elements to list with integers
    for item in searched_text:
        try:
            li.append(int(item))
        except ValueError:
            continue

    return li
if __name__ == '__main__':

    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')


def flat_list(array):
    tot = list()
    for x in array:
        if not isinstance(x, list):
            print(x)
            tot.append(x)
        else:
            flat_list(x)
    print(tot)
    return tot

if __name__ == '__main__':

    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')