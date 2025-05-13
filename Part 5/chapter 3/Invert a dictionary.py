def invert(dictionary: dict):
    inverted = {value: key for key, value in dictionary.items()}
    dictionary.clear()
    dictionary.update(inverted)


s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)