while True :
    try :
        text = str(input("Please type in a string: "))
        
        len_text = len(text)
        index = 20 - len_text

        if text == '1' :
            break
        else :
            print("*" * index + str(text))
    except ValueError :
        print("Please try again. ")