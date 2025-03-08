while True :
    try :
        word = str(input("Word(if you want to exit, type 'exit'): "))

        if word.lower() == "exit":  
            break

        len_word = len(word)
        a = len_word // 2
        b = 14 - a

        print("*" * 30) 

        if len_word % 2 != 0:
            b -= 1  

        print("*" + " " * b + word + " " * b + "*")  

        print("*" * 30) 
    except ValueError :
        print("Please try again. ")