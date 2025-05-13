def same_chars(word,index_1,index_2) :
    if word[index_1] == word[index_2] :
        print("indexes have the same letter")
    else :
        print("indexes have'the same letter")

while True:
    try:
        word = str(input("what is the length of the string(if you want to exit, type '1'): "))

        if word == '1' :
            break

        index_1 = int(input("what is the length of the index: "))
        index_2 = int(input("what is the length of the index: "))

        same_chars(word,index_1,index_2)
    except ValueError :
        print("Please try again.")  