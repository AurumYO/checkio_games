from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:
    fin = els[:2]
    if len(els) <= 2:
        return els
    else:
        for i in range(2, len(els)):
            sub_els = els[i-2:i+1]
            min_value, max_value = min(sub_els), max(sub_els)
            sub_els.remove(min_value)
            sub_els.remove(max_value)
            fin += sub_els
        return fin


if __name__ == '__main__':
    print( "Example:" )
    print( list( median_three( [1, 2, 3, 4, 5, 6, 7] ) ) )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list( median_three( [1, 2, 3, 4, 5, 6, 7] ) ) == [1, 2, 2, 3, 4, 5, 6]
    assert list( median_three( [1] ) ) == [1]
    assert list(median_three([-1, 0, 1])) == [-1, 0, 0]
    assert list(median_three([5,2,9,1,7,4,6,3,8])) == [5,2,5,2,7,4,6,4,6]
    print("Coding complete? Click 'Check' to earn cool rewards!")