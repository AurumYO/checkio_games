def checkio(crossword, words):

    def lines_graph(crossword, words):
        # find ciphered all lines with words
        line_numbers = {}
        counter = 1
        for i in range(len(crossword)):
            if 0 not in crossword[i]:
                line_numbers[counter] = crossword[i]
                counter +=1
        diognal = []
        for i in range(len(crossword)):
            for j in range(len(crossword)):
                if crossword[j][i] != 0:
                    diognal.append(crossword[j][i])
            if len(diognal) >= len(min(words)):
                line_numbers[counter] = diognal
                counter += 1
            diognal = []
        return line_numbers

    def letters_dict(crossword):
        crossword_letters = {}
        for i in range(len(crossword)):
            for d in crossword[i]:
                if d not in crossword_letters.keys():
                    crossword_letters[d] = None
        return crossword_letters

    def numbers_dict(words):
        letters_dict = {}
        for word in words:
            for l in word:
                if l not in letters_dict.keys():
                    letters_dict[l] = None
        return letters_dict

    def words_lister(words):
        words_list = {i: [] for i in range(1, len(words))}
        for i in range(len(words)):
            listed_word = []
            for char in words[i]:
                 listed_word.append(char)
            words_list[i+1] = listed_word
            listed_word = []
        return words_list

    wl = words_lister(words )
    nd = letters_dict(crossword)
    ln = lines_graph( crossword, words )
    ld = numbers_dict(words)

    # print(ld, len(ld))
    # print(nd, len(nd))
    # # print(crossword)
    # print(wl)
    # print(ln)

    # returns list of letters from which new word starts
    def start_letters_list(words):
        start_letters = []
        for word in words:
            start_letters.append(word[0])
        print(start_letters)
        return start_letters

    # returns list of numbers which are in the beginning of a word
    def start_numbers(ln):
        start_numbers = []
        for word in ln.values():
            start_numbers.append(word[0])
        print(start_numbers)
        return start_numbers

    # try if word fits into line of the graph
    def try_word(words, line):
        approp_words = []
        for word in words:
            if len(word) == len(line):
                approp_words.append(word)
        print(approp_words)
        return approp_words

    # place word in line
    def try_place_word(word, line, filled_dict):
        new_line = []
        for num in range(len(line)):
            if num == 0 and num not in filled_dict.get(line[num]):
                filled_dict[line[num]] = word[num]
        print(new_line, filled_dict)




    def place_word(crossword, start_let, start_num, words, num_list):
        graph = crossword
        filled_dict = {}
        for line in crossword:
            if line in num_list.values():
                ap = try_word(words.values(), line)
                for tw in ap:
                    try_filled_line = try_place_word(tw, line, filled_dict)
                    print(try_filled_line)

        pass

    st_let = start_letters_list(words)
    st_num = start_numbers(ln)
    pl = place_word(crossword, st_let, st_num, wl, ln)

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
