def checkio(crossword, words):

    def lines_graph(crossword, words):
        # find ciphered all lines with words
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
        # print(line_numbers)  # display all ciphered words
        return line_numbers


    def letters_dict(crossword):
        crossword_letters = {}
        for i in range(len(crossword)-1):
            for d in crossword[i]:
                if d not in crossword_letters.keys():
                    crossword_letters[d] = None
        return crossword_letters


    def words_lister(words):
        words_list = [[] for i in range(len(words)-1)]
        for i in range(len(words)-1):
            for char in words[i]:
                words_list[i].append(char)
        # print(words_list)
        return words_list

    wl = words_lister( words )
    ld = letters_dict(crossword)
    ln = lines_graph( crossword, words )

    print(ld)
    print(crossword)
    print(wl)
    print( ln )




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
