def checkio(str_number: str, radix: int) -> int:
    try:
        number = int(str_number, radix)
        return number
    except ValueError:
        return -1


    # import string
    # alfa = '0123456789'+string.ascii_uppercase
    # res = 0
    # for chr in str_number:
    #     if alfa.index(chr) + 1 > radix:
    #         print(alfa.index(chr), 'alfa')
    #         res = -1
    #         break
    #     else:
    #         pass
    # if res != -1:
    #     i = 0
    #     for chr in str_number[::-1]:
    #         print(alfa.index(chr), 'alfaes')
    #         print(res, radix, 'radix', i, 'index')
    #         res = res + alfa.index(chr)*radix**i
    #         print(res,'result')
    #         i += 1
    # print (res)
    # return res


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
