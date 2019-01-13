def to_encrypt(text, delta):
    ltext = list()
    for i, ch in enumerate(text):
        if ch <= chr(122) and ch != chr(32):
            if delta >= 0:
                nch = chr(ord(ch) + delta)
                if nch <= chr(122):
                    ltext.append(nch)
                elif nch > chr(122):
                    nch = chr(ord(nch) - 26)
                    ltext.append(nch)
            if delta < 0:
                nch = chr(ord(ch) + delta)
                if nch >= chr(97):
                    ltext.append(nch)
                elif nch <= chr(96):
                    nch = chr(ord(nch) + 26)
                    ltext.append(nch)
        else:
            ltext.append(ch)

    return ''.join(ltext)


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")