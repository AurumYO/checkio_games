# this function defines the age of the ghost from new born (opacity 10000) to too old (with opacity less than 5000)
def checkio(opacity):
    fibo_list = []
    a, b = 0, 1
    for i in range(20):
        a, b = b, a + b
        fibo_list.append(b)

    born_opacity = 10000
    gost_age = 0
    while opacity != born_opacity:
        gost_age += 1
        if gost_age in fibo_list:
            born_opacity -= gost_age
        if gost_age not in fibo_list:
            born_opacity += 1
    return gost_age


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(3703) == 4665, "4665 years"
    assert checkio(9990) == 5, "5 years"
    assert checkio(6736) == 3516, "3516 years"
