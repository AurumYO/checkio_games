def two_teams(sailors):
    # replace this for solution
    over_under = [] #creating a new empty list for sailor's names under 20y.o and ove 40y.o
    in_mid = []#creating a new empty list for sailor's names between 20 and 40 y.o.
    for k, v in sailors.items(): #loping through dict with teams by parsing its keys and values to list
         if v >= 40 or v <= 20 : #if value of key in dictinary (sailor's age) under 20 and over 40 appending to 1st list
            over_under.append(k)
            over_under_team = sorted(over_under) #creating sorted list
         if v >= 20 and v <= 40 : # if value over 20 and uder 40 apending sailor to the second list
            in_mid.append(k)
            inthemid_team = sorted(in_mid)#creating sorted list of sec team

    return [
        over_under_team,
        inthemid_team
    ]  # returning result of function in two lists of 1 team aged under 20&over 40 and second team aged over 20 & under 40

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert two_teams({
#        'Smith': 34,
#        'Wesson': 22,
#        'Coleman': 45,
#        'Abrahams': 19}) == [
#               ['Abrahams', 'Coleman'],
#               ['Smith', 'Wesson']
#           ]
#
#    assert two_teams({
#        'Fernandes': 18,
#        'Johnson': 22,
#        'Kale': 41,
#       'McCortney': 54}) == [
#               ['Fernandes', 'Kale', 'McCortney'],
#               ['Johnson']
 #          ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
