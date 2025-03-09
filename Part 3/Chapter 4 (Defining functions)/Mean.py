def mean(number_1, number_2, number_3) :
    total = number_1 + number_2 + number_3
    print(total/3)


while True :
    try:
        number_1 = int(input("Please type in a number(if you want to exit, type negative  numbers): "))

        if number_1 < 0 :
            break

        number_2 = int(input("Please type in a number: "))
        number_3 = int(input("Please type in a number: "))

        mean(number_1,number_2,number_3)

    except ValueError:
        print("Please try again.")