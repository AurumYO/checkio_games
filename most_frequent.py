def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    di = {}
    for i in data:
        di[i] = di.get(i, 0) + 1
    max_key = max(di, key=di.get)
    return max_key


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
