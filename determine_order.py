
def checkio(data):

    def check_if_data_empty(data):
        """
        This function checks if provided data array consists of empty data structures
        :param data: data structure with some data inside
        :return: True if data has some values, False is data array is empty
        """
        score = len(data)
        for item in data:
            if len(item) == 0:
                score -= 1
        if score == 0:
            return False
        return True

    def sort_alphabetically(data):
        """
        This function sorts
        :param data: list with some data
        :return: sorted in ascending order string with letters
        """
        all_letters = []
        for item in data:
            if item not in all_letters:
                all_letters.append(item)
        return ''.join(sorted(all_letters))

    def check_if_all_have_different_letters(data):
        """
        :param data: list of data
        :return: sorted in ascending order string of characters if provided data consists of unique characters,
        or returns True if provided data has repeated characters
        """
        letters_section = []
        counter = 0
        for item in data:
            for i in item:
                counter += 1
                if i not in letters_section:
                    letters_section.append(i)
        if len(letters_section) == counter:
            return sort_alphabetically(letters_section)
        else:
            False

    # convert data into list of dictionaries representing each "word" , where key is letter and value is its index
    def convert_to_tuple(data):
        """
        This function converts data from strings to list of tuples
        :param data: list with items consisting of words as strings data
        :return: list with words represented as lists where each letter in word represented as tuple with letter and
        letter's index position in word
        """
        dataset = []
        for item in data:
            li_items = []
            count = 0
            for let in item:
                li_items.append(tuple((let, count)))
                count += 1
            dataset.append(li_items)
        return dataset

    def check_if_next_standing(candidates, index, data):
        combinations = []
        searched_letters = candidates.copy()
        found_letters = []
        for d in data:
            new_combination = []
            searched_letters = candidates.copy()
            found_letters = []
            for pair in d:
                if pair[0] in searched_letters and pair[0] not in found_letters:
                    found_letters.append(pair[0])
                    new_combination.append(pair)
                if len(new_combination) == len(candidates):
                    combinations.append(d)
                    new_combination = []

        # find neighbors
        neigbors = []
        for item in combinations:
            new_item = []
            for i in range(len(item)):
                if item[i][0] in candidates:
                   new_item.append(item[i])
            neigbors.append(new_item)

        # find letter with maximal index position of candidate letters within neighboring letters
        max_position_dict = dict.fromkeys(candidates, 0)
        for item in neigbors:
            for pair in item:
                if pair[0] in max_position_dict.keys() and max_position_dict[pair[0]] < pair[1]:
                    max_position_dict[pair[0]] = pair[1]

        first_neigbor = ''
        for k, v in max_position_dict.items():
            if v < index:
                first_neigbor = k

        return first_neigbor


    def find_best_candidate(candidates, data):
        if len(candidates) == 1:
            return candidates[0]
        else:
            max_indexes_dict = dict.fromkeys(candidates, 0)
            min_indexes_dict = dict.fromkeys(candidates, 0)
            researched_data = []
            for item in data:
                for pair in item:
                    if pair[0] in candidates:
                        researched_data.append(pair)
                        if max_indexes_dict[pair[0]] < pair[1]:
                            max_indexes_dict[pair[0]] = pair[1]
                        if min_indexes_dict[pair[0]] > pair[1]:
                            min_indexes_dict[pair[0]] > pair[1]


            candidates_dict = {}
            minimal_difference = max(max_indexes_dict.values())
            for k, v in max_indexes_dict.items():
                if max_indexes_dict[k] == min_indexes_dict[k]:
                    candidates_dict.update({k : v})
                elif max_indexes_dict[k] != min_indexes_dict[k]:
                    difference_within_keys = max_indexes_dict[k] - min_indexes_dict[k]
                    if difference_within_keys < minimal_difference:
                        minimal_difference = difference_within_keys

            if (len(candidates_dict)) == 1:
                return list(candidates_dict.keys())[0]

            if len(candidates_dict) > 0 and max(candidates_dict.values()) == 0:
                keys_to_check = sort_alphabetically([*candidates_dict])
                return keys_to_check

            scores = {}
            for k, v in max_indexes_dict.items():
                if v not in scores:
                    scores[v] = [k]
                elif v in scores:
                    scores[v] += [k]

            if minimal_difference in scores.keys() and len(scores[minimal_difference]) == 1:
                return ''.join(scores[minimal_difference])

            for k, v in scores.items():
                if k == 0 and len(v) == 1:
                    return ''.join(v)
                elif k == 0 and len(v) > 1:
                    sort_alpha = sort_alphabetically(v)
                    return sort_alpha
                elif k > 0 and len(v) > 1:
                    best_of_many_candidates = check_if_next_standing(v, k, data)
                    return best_of_many_candidates
                elif k > 0 and len(v) == 1:
                    min_key = min(scores.keys())
                    best_candidate = scores[min_key]
                    return ''.join(best_candidate)

    def check_first_possible(data_list):
        first_letters = []
        for n in range(len(data_list)):
            for pair in data_list[n]:
                if pair[1] == 0:
                    first_letters.append(pair[0])
        best_candidate = find_best_candidate(first_letters, data_list)
        return best_candidate

    def change_index(old_value, candidate_letter):
        new_value = []
        shift = 0
        for pair in old_value:
            if candidate_letter in pair:
                shift += 1
            if candidate_letter not in pair:
                new_value.append(tuple((pair[0], pair[1] - shift)))
        return new_value

    def remove_candidate_from_data(candidate, remaining_data):
        new_data = []
        let_alpha = candidate
        for n in range(len(remaining_data)):
            new_section = None
            if len(remaining_data[n]) == 0:
                pass
            elif remaining_data[n][0][0] == candidate:
                new_section = change_index(remaining_data[n], candidate )
                new_data.append(new_section)
            elif remaining_data[n][0][0] != candidate:
                new_data.append(remaining_data[n])

        return let_alpha, new_data

    res = ''
    check_if_data_different_letters = check_if_all_have_different_letters(data)
    if check_if_data_different_letters:
        return check_if_data_different_letters
    else:
        converted_data = convert_to_tuple(data)
        data_not_empty = True
        while data_not_empty:
            first_possible = check_first_possible(converted_data)
            if len(first_possible) > 1:
                for l in first_possible:
                    letter_to_alphabet, converted_data = remove_candidate_from_data(l, converted_data )
                    res += l
                    data_not_empty = check_if_data_empty( converted_data )
            else:
                letter_to_alphabet, converted_data = remove_candidate_from_data( first_possible, converted_data )
                res += letter_to_alphabet
                data_not_empty = check_if_data_empty( converted_data )

        return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["a", "d", "c"]) == "acd", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
    assert checkio( ["hello", "low", "lino", "itttnosw"]) == "helitnosw"
    assert checkio( ["xxxyyz", "yyww", "wwtt", "ttzz"] ) == "xywtz"
    assert checkio(["axton","bxton"]) == "abxton"
    assert checkio(["bxton","dxton"]) == "bdxton"
    assert checkio(["jhgfdba","jihcba","jigedca"]) == "jihgefdcba"
    assert checkio(["ghi","abc","def"]) == "abcdefghi"
