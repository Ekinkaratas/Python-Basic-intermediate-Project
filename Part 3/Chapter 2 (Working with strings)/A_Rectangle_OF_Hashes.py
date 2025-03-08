while True :
    try :
        width = int(input("Width(if you want to exit, type in be negative integer): "))
        height = int(input("Height(if you want to exit, type in be negative integer): "))

        if width < 0 or height < 0 :
            break
        else :
            for i in range(height) :
                print(width * "#")
    except ValueError :
        print("Please type in be positive integer.  ")