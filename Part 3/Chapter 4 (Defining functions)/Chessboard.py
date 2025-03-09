def chessboard(length) :
    # Can be solved in 2 ways

        #Solution 1
        #for i in range(length):  # Satırları kontrol et
        #    number = i % 2  # Satır numarası çiftse 0, tekse 1 ile başlar
        #    for _ in range(length):
        #        print(number, end="")
        #        number = 1 - number  # 0 ise 1 yap, 1 ise 0 yap
        #    print() 
    
    #Solution 2
    control = 0
    while control < length :
        number = 1
        for _ in range(length) :
            print(number,end="")
            if number == 1 :
                number = 0 ;
            else :
                number = 1
        control +=1
        print()

        if control == length :
            continue

        number = 0
        for _ in range(length) :
            print(number,end="")
            if number == 1 :
                number = 0 ;
            else :
                number = 1
        print()
        control +=1


while True:
    try:
        number = int(input("Please type in a number(if you want to exit, type negative numbers or zero): "))

        if number == 1 :
            print("number must be greater than 1")
            continue

        if number <= 0 :
            break

        chessboard(number)
    except ValueError :
        print("Please try again.")     