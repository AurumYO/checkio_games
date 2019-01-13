def house(plan):
    char = '#'
    # create new list by splitting our plan to lines by '\n'
    li_plan = plan.strip().split('\n')
    # Initilize new list were we will put positions of our '#' character in each separate line
    # add +1 to each position to avoid zero division in case searched '#' in position with index 0
    width_list = []
    for line in enumerate(li_plan):
        for element in enumerate(line[1]):
            if element[1] == char:
                position = element[0] + 1
                width_list.append(position) # Append position to searcher character to the new list
    # If we have not founr '#' in any of lines  - return 0 (no characters found)
    if len(width_list) == 0:
        return 0
    # Defining min and max positions to calculate the width of the house
    # from minimal position extracted -1 to revert the length of the original line from plan
    min_position, max_position = min(width_list), max(width_list)
    house_width = max_position - (min_position - 1)

    # define the lenth of the house iterating through lines
    house_length = 0
    for line in li_plan:
        if char in line: # if '#' in line increase the length of the house by 1
            house_length += 1
        # In case if we have inside our plan lines with no '#' we choul also include such lilnes to our house length
        if char not in line and max_position > 0 and line != li_plan[0]:
            house_length += 1
    # Find house area by multiplying lenth of house by its width
    size_of_house = house_width * house_length
    return size_of_house


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

    assert house('''00#
0#0
#00
''') == 9

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
    assert house('''0000000000
0000000000
#00000000#
##########
##00000000
#000000000
''') == 40
    assert house('''
0000000000
000###0000
000#######
000###0000
''') == 21

    print("Coding complete? Click 'Check' to earn cool rewards!")
