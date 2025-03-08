while True :
    try :
        word = str(input("Please type in string(if you want to exit, type '1'): "))
        if word != "1" :
            for i in range(len(word)-1, -1 , -1) :
                print(f"'{word[i]}' ", end="")
            print("")
        else :
            break
    except ValueError :
        print("Please try again. ")