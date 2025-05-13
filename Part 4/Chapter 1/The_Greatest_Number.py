def The_Greatest_Number(number_1,number_2,number_3) :
    if number_1 == number_2 == number_3 :
        print("All numbers equal")
    else:
        greatest_number = max(number_1,number_2,number_3)
        print(f"Largest number {greatest_number}")

while True:
    try:
        number_1 = int(input("what is the length of the number(if you want to exit, type negative numbers or zero): "))

        if number_1 <= 0 :
            break

        number_2 = int(input("what is the length of the number: "))
        number_3 = int(input("what is the length of the number: "))

        The_Greatest_Number(number_1,number_2,number_3)
    except ValueError :
        print("Please try again.")  