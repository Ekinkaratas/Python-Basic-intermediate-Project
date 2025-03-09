while True :
    try :
        number = int(input("Please type in a number(if you want to exit, type negative numbers or zero): "))

        if number <= 0 :
            print("Thanks and bye!")
            break

        if number == 1 :
            print("The factorial of the number 1 is 1")
        else :
            total = 2

            for i in range(3,number+1,1) :
                total *= i

            print(f"The factorial of the number {number} is {total}")    
    except ValueError :
        print("Please try again. ")