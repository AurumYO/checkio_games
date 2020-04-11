
def is_majority(items: list) -> bool:
    counter_true, counter_false = 0, 0
    for item in items:
        if item:
            counter_true += 1
        else:
            counter_false += 1
    if counter_true > counter_false:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")