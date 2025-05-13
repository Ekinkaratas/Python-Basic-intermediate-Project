def list_of_stars(inputList) :
    for var in inputList :
        print("*" * var)

while True:
    try:
        my_list = []
        number = int(input("Please type in a word(if you want to exit, type negative numbers or zero): "))
        my_list.append(number)
        if number <= 0:
            break

        number_2 = int(input("Please type in a word: "))
        number_3 =int(input("Please type in a word: "))
        my_list.append(number_2)
        my_list.append(number_3)
        

        list_of_stars(my_list)
    except ValueError:
        print("Please try again.")
        