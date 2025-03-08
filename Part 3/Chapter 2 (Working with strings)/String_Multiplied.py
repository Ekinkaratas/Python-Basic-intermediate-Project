while True :
    try :
        word = str(input("Please type in a string(if you want to exit, type '1'): "))
        amount = int(input("Please type in an amount: "))

        if word != "1":
            print(word * amount)
        else :
            break
    except ValueError :
        print("Please try again. ")