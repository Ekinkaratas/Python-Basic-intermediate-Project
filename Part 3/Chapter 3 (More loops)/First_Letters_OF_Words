while True :
    try :
        text = str(input("Please type in a string(if you want to exit, type '1'): "))

        if text == '1' :
            break

        print(text[0])
        
        index = text.find(" ")
        while index != -1 :
            if index + 1 < len(text):
                char_FOUND = text[index+1]
                print(char_FOUND)
            index = text.find(" ",index+1)
        

    except ValueError :
        print("Please try again. ")