while True :
    try :
        text = str(input("Please type in a string(if you want to exit, type 'exit'): "))
        len_text = len(text)

        if text.lower() == 'exit' :
            break

        for i in range(1,len_text+1,1):
            print(text[0:i])
    except ValueError :
        print("Please try again. ")