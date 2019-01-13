def house(plan):
    char = '#'
    width = 0
    length_house = 0
    plan = plan.rstrip().lstrip().split('\n')

    for line in plan:
        if char in line:
            width += 1
            #line = line.strip('0')
        li = [i for i, e in enumerate(line) if e == char]
        if len(li) >= 1:
            length_house = (max(li) + 1)

        elif len(li) == 0:
            length_house = 0
        print(li)
        if char not in line and width > 0 and line != plan[0]:
            width += 1
    print(length_house, width)
    res = length_house * width
    print(res)
    return res

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12
    assert house('''
0000000000
#00000000#
##########
##00000000
#000000000
    ''') == 40

    print("Coding complete? Click 'Check' to earn cool rewards!")
