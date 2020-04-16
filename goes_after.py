def goes_after(word: str, first: str, second: str) -> bool:
    word_first = word.find(first)
    word_second = word.find(second)
    if word_second > word_first and first + second == word[word_first:word_second+1]:
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after("almaz","m","a") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")