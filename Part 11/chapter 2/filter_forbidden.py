def filter_forbidden(string: str, forbidden: str):
    return "".join([word for word in string if word not in forbidden])

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)