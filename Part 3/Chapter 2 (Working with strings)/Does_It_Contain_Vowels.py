while True :
    try :
        text = str(input("Please type in a string(if you want to exit, type 'exit'): "))
        len_text = len(text)

        if text.lower() == "exit":
            break
        
        len_text = len(text)

        if text.find('a') != -1:
            print("a found")
        else:
            print("a not found")
        
        if text.find('e') != -1:
            print("e found")
        else:
            print("e not found")
        
        if text.find('o') != -1:
            print("o found")
        else:
            print("o not found")
    except ValueError :
        print("Please try again.")