def safe_pawns(pawns: set) -> int:
    # Step one we create from asserted set of string values to new set with
    # pair of two numbers in range from 1 to 8
    new_set = set()
    for pawn in pawns:
        l = ord(pawn[0]) - ord('a') + 1
        d = int(pawn[1])
        new_set.add((l, d))

    # Step 2: we use new set from numbers as coordinates in matrix and iterate
    # through the new set to check if pawn in safe position and return count of
    # safe positions
    counter = 0
    for point in new_set:
        l, d = point[0], point[1]
        new_d = d - 1
        new_l1 = l + 1
        new_l2 = l - 1
        if (new_l1, new_d) in new_set or (new_l2, new_d) in new_set:
            counter += 1

    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# def safe_pawns(data: set) -> int:
#
#     safe = 0
#
#     for i in data:
#
#         # split the string by number(n) and letter(l)
#
#         loc = i
#
#         n, l = ord(i[0]), int(i[1])
#
#
#         # pawn protector locations
#
#         protector = {chr(n - 1) + str(l - 1), chr(n + 1) + str(l - 1)}
#         print(protector)
#
#
#         # find out if there are pawns below to protect it
#
#         if (any(x in data for x in protector)):
#
#             safe += 1
#
#     return (safe)
#
def safe_pawns(pose):

    file = ['a','b','c','d','e','f','g','h'] #creating the file to get index latter

    count =[]

    for p in list(pose):

        len(pose)

        i = file.index(p[0])# take the index if the current pawn

        #in the next step we check if the index -1  and index +1

        #in the file is exist in the positions we have or not

        #if it's exist we toke those position and put it in either j or k

        if file[i] == 'a' :

            j= None

            k=[n for n in pose if (n[0]==file[i+1])]

        elif file[i] == 'h':

            j= [n for n in pose if n[0]==file[i-1]]

        else :

            j= [n for n in pose if n[0]==file[i-1]]

            k=[n for n in pose if (n[0]==file[i+1])]

        if j : # check if j is empty or not

            count.extend([p for pos in j if int(p[1])-int(pos[1]) ==1 ])

            #now we check if the row is lower than the current item position by 1

        if  k :# check if k is empty or not

            count.extend([p for pos in k if int(p[1])-int(pos[1]) ==1 ])

    return len(set(count))





# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
#     assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")