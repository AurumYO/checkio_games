class Friends:
    def __init__(self, connections):
        self.name = connections

    def add(self, connection):
        self.connection = connection
        if self.connection not in self.name:
            new = []
            new.append(self.connection)
            for x in self.name:
                new.append(x)
            self.name = new
            return True
        return False

    def remove(self, connection):
        self.connection = connection
        if self.connection in self.name:
            new = []
            for pair in self.name:
                if pair != connection:
                    new.append(pair)
            self.name = new
            return True
        else:
            return False

    def names(self):
        items_names = []
        for item in self.name:
            for n in item:
                if n not in items_names:
                    items_names.append(n)
        return set(sorted(items_names))

    def connected(self, name):
        self.neighbor = name
        connected_items = []
        for pair in self.name:
            if self.neighbor in pair:
                for neighbor in pair:
                    if neighbor not in connected_items and self.neighbor != neighbor:
                        connected_items.append(neighbor)
        return set(connected_items)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"