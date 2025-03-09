while True :
    try :
        number = int(input("Please type in a number(if you want to exit, type negative numbers or zero): "))

        if number <= 0 :
            print("Thanks and bye!")
            break  
        
        i=1
        while i <= number :
            if number == i :
                print(i)
            else :
                print(i)
                print(number)
            i +=1
            number -=1
    except ValueError :
        print("Please try again. ")