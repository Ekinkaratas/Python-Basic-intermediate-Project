while True :
    try :
        word_1 = str(input("Please type in string 1(if you want to exit, type 'exit'): "))
        word_2 = str(input("Please type in string 2: "))

        len_word_1 = len(word_1)
        len_word_2 = len(word_2)

        if word_1 != "exit" :
            if len_word_1 > len_word_2 :
                print(f"{word_1} bigger than {word_2}")
            elif len_word_2 > len_word_1 :
                print(f"{word_2} bigger than {word_1}")
            else :
                print("Two words equal")
        else :        
            break
    except ValueError :
        print("Please try again. ")