def histogram(word : str):
    new_dict = {char: "*"*word.count(char) for char in word}

    for key in new_dict:
        print(f"{key} : {new_dict[key]}")

histogram("statistically")