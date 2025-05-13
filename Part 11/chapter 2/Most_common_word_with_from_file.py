import os
from collections import Counter

os.chdir(os.path.dirname(__file__))

import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename, encoding='utf-8') as file:
        text = file.read().lower()

    # Noktalama işaretlerini temizle
    for ch in string.punctuation:
        text = text.replace(ch, " ")

    # Kelimelere ayır
    words = text.split()

    # Kelime frekanslarını say
    word_counts = Counter(words)

    # Belirtilen eşikten büyük olanları filtrele
    common = {word: count for word, count in word_counts.items() if count >= lower_limit}

    print(common)

most_common_words("comprehensions.txt", 2)
