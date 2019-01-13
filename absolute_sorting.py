def checkio(numbers_array: tuple) -> list:
    #return sorted(numbers_array, key=abs)

    # optional creative solution
    mytuple = ()
    mydict = {}
    mydict_new = {}

    # Create a dictionary
    for i in numbers_array:
        mydict[abs(i)] = i
    print(mydict)
    # Sort dictionary by key
    for key in sorted(mydict):
        mydict_new[key] = mydict[key]
    print(mydict_new)
    # Return a tuple of dictionary values
    for v in mydict_new.values():
        mytuple += (v,)
        print(mytuple)
    return mytuple

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
