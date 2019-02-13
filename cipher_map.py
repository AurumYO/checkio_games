def recall_password(cipher_grille, ciphered_password):
    # this function gets points where letters are hidden
    def get_points(cipher_grille):
        char = 'X'
        points = []
        for x in enumerate(cipher_grille):
            for y in enumerate(x[1]):
                if y[1] == char:
                    # print(x[0], ' is x')
                    # print(y[0], 'is y')
                    points.append((x[0], y[0]))
        # print(points[0])
        return points

    # this function rotates the points with hidden letters by 90 degrees
    def rotate_cipher_grille(points):
        new_points = []
        for point in points:
            x, y = point[1], abs(point[0] - 3)
            # print('new point ', x, y)
            new_points.append((x, y))
        return new_points

    # this function deciphrates the password
    def get_password(ciphered_password, all_points):
        letters_cord = dict()
        for x in enumerate(ciphered_password):
            for y in enumerate(x[1]):
                letters_cord[(x[0], y[0])] = y[1]
        # print(letters_cord)
        password = str()
        for c in all_points:
            for k in letters_cord.keys():
                if c == k:
                    password += letters_cord[k]
        # print(password)
        return password

    # very basic game logic taking in account precondition
    points = get_points(cipher_grille)
    all_points = list(sorted(points))
    # print(all_points, 'first row')
    points = rotate_cipher_grille(points)
    all_points += sorted(points)
    # print(all_points, 'second row')
    points = rotate_cipher_grille(points)
    all_points += sorted(points)
    # print(all_points, 'third row')
    points = rotate_cipher_grille(points)
    all_points += sorted(points)
    # print(all_points, 'forth row')
    password = get_password(ciphered_password, all_points)
    return password


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
