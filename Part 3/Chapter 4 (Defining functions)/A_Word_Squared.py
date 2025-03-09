def chessboard(text,length) :
    len_text = len(text)
    for i in range(length):  
        number = i % len_text  
        for _ in range(length):
            print(text[number], end="")
            number = (number + 1) % len_text 
        print() 

while True:
    try:
        text = str(input("Please type in a string(if you want to exit, type '1'): "))

        if text == "1" :
            break

        number = int(input("what is the length of the square: "))

        chessboard(text,number)
    except ValueError :
        print("Please try again.")  