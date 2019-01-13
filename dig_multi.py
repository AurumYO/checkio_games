
def checkio(number: int) -> int:
    numbers = str(number)
    print(numbers)
    result = int(numbers[0])
    print(result, 'first')
    for num in numbers[1:]:
        if int(num) != 0:
            print(int(num))
            result = result * int(num)
            print(result, 'result')
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")