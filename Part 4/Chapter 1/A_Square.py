def square(word,length) :
    for _ in range(length) :
        print(word * length)
            

while True:
    try:
        word = str(input("Please type in a word(if you want to exit, type '1'): "))

        if word == "1" :
            break

        number = int(input("what is the length of the square: "))

        square(word,number)
    except ValueError :
        print("Please try again.")  