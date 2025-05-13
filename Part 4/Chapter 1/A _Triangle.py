def triangle(word,length) :
    for i in range(1,length+1,1) :
        print(" " * (length - i), end="")
        print(word * (2 * i - 1))


while True:
    try:
        word = str(input("Please type in a word(if you want to exit, type '1'): "))

        if word == "1" :
            break

        number = int(input("what is the length of the triangle: "))

        triangle(word,number)
    except ValueError :
        print("Please try again.")  