from typing import List


def checkio(game_result: List[str]) -> str:
    if game_result[0][0] != '.' and game_result[0][0] == game_result[1][0] and game_result[0][0] == game_result[2][0]:
        res = str(game_result[0][0])
    elif game_result[0][1] != '.' and game_result[0][1] == game_result[1][1] and game_result[0][1] == game_result[2][1]:
        res = str(game_result[0][1])
    elif game_result[0][2] != '.' and game_result[0][2] == game_result[1][2] and game_result[0][2] == game_result[2][2]:
        res = str(game_result[0][2])
    elif game_result[0][0] != '.' and game_result[0][0] == game_result[1][1] and game_result[0][0] == game_result[2][2]:
        res = str(game_result[0][0])
    elif game_result[0][2] != '.' and game_result[0][2] == game_result[1][1] and game_result[0][2] == game_result[2][0]:
        res = str(game_result[0][2])
    elif game_result[0][0] != '.' and game_result[0][0] == game_result[0][1] and game_result[0][0] == game_result[0][2]:
        res = str(game_result[0][0])
    elif game_result[1][0] != '.' and game_result[1][0] == game_result[1][1] and game_result[1][0] == game_result[1][2]:
        res = str(game_result[1][0])
    elif game_result[2][0] != '.' and game_result[2][0] == game_result[2][1] and game_result[2][0] == game_result[2][2]:
        res = str(game_result[2][0])
    else:
        res = "D"

    return res


if __name__ == '__main__':
    print("Example:")
    print(checkio(["...",
                   "XXX",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio([
        "...",
        "XXX",
        "XOO"]) == "X", "Xs wins again"
