while True :
    try :
        number = int(input("Please type in a number(if you want to exit, type negative numbers): "))
        
        if number < 0 :
            break

        for i in range(1,number+1,1) :
            number_LEFT = i
            for j in range(1,number+1,1) :
                number_RIGHT = j
                total = number_LEFT * number_RIGHT
                print(f"{number_LEFT} X {number_RIGHT} = {total}")

    except ValueError :
        print("Please try again. ")