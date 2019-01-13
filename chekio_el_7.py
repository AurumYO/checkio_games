def best_stock(data):
    for k, v in data.items():
        v_max = max(data.values())
        if v == v_max:
            pass


def best_stock(data):
    print(max(data, key=data.get))
    print(type(max(data, key=data.get)))

    # These "asserts" are used for self-checking and not for an auto-testing


assert best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}) == 'ATX', "First"
assert best_stock({
    'CAC': 91.1,
    'ATX': 1.01,
    'TASI': 120.9
}) == 'TASI', "Second"
print("Coding complete? Click 'Check' to earn cool rewards!")