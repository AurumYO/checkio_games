def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """
    if n >= 0 and n < len(array):
        s = array[n]
        res = s ** n
        return res
    else:
        res = -1
        return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    assert index_power([96, 62, 94], 3) == -1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")