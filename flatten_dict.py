def flatten(dictionary):
    # loop thought each key: value pair,
    for key, val in dictionary.items():
        # change value of the dictionary's key to empty space if value is empty dictionary
        if isinstance(val, dict) and len(val) == 0:
            dictionary[key] = ""
        # if value of the dictionary's key is inner dictionary with some items
        if isinstance(val, dict) and len(val) > 0:
            # create ne dictionary with corrected key name to path format separating names of inner keys with '/'
            corrected_dict = {key + '/' + inner_key: inner_val for inner_key, inner_val in val.items()}
            # remove current key:value pair from original dictionary
            dictionary.pop(key)
            # update newly created dictionary with corrected names of keys with the remaining part of the dictionary
            corrected_dict.update(dictionary)
            # call function again providing as argument new corrected dictionary
            return flatten(corrected_dict)

    # function returns flatted dictionary
    return dictionary


if __name__ == '__main__':
    # test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    # print(' Input: {}'.format(test_input))
    # print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')