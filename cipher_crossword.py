def checkio(crossword, words):


    line_numbers = []
    for i in range(len(crossword)):
        if 0 not in crossword[i]:
            line_numbers.append(crossword[i])
    diognal = []
    for i in range(len(crossword)):
        for j in range(len(crossword)):
            if crossword[j][i] != 0:
                diognal.append(crossword[j][i])
        if len(diognal) >= len(min(words)):
            line_numbers.append(diognal)
        diognal = []

    print(line_numbers)

    letters_dict = {}
    for word in words:
        for let in word:
            if let not in letters_dict.keys():
                letters_dict[let] = 1
            else:
                letters_dict[let] += 1
    print(letters_dict)


    # num_dict = {}
    # for line in crossword:
    #     for n in line:
    #         if n == 0:
    #             num_dict[' '] = ' '
    #         elif n not in num_dict.keys():
    #             num_dict[n] = 1
    #         else:
    #             num_dict[n] += 1
    # for k, v in letters_dict.items():
    #     for num, occ in num_dict.items():
    #         if v == occ:
    #             print('letter', k, 'has num', num)
    #
    # print( letters_dict, num_dict)
    return None


if __name__ == '__main__':
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6]
        ],
        ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']) == [['h', 'e', 'l', 'l', 'o'],
                                                                    ['a', ' ', 'e', ' ', 'z'],
                                                                    ['b', 'i', 'm', 'b', 'o'],
                                                                    ['i', ' ', 'm', ' ', 'n'],
                                                                    ['t', 'r', 'a', 'c', 'e']]
