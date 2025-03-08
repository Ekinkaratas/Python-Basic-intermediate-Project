while True :
    try :
        text = str(input("Please type in a string(if you want to exit, type in be '1'): "))
        len_text = len(text)

        if text == '1' :
            break
        else :
            print(text)
            print(len_text * '-')
            
    except ValueError :
        print("Please try again. ")