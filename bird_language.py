VOWELS = "aeiouy"

def translate(phrase):
    new = str()
    count = 0
    for i in range(len(phrase)):
        if phrase[i] in VOWELS:
            count += 1
            if count == 3:
                new += phrase[i]
                count = 0
        elif phrase[i] not in VOWELS:
            new += phrase[i]
            count = 0
    return new

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"