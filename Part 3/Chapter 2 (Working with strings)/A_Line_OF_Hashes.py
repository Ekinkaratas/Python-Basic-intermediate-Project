while True :
    try :
        width = int(input("Width(if you want to exit, type in be negative integer): "))

        if width < 0 :
            break
        else :
            print(width * "#")
    except ValueError :
        print("Please type in be positive integer.  ")