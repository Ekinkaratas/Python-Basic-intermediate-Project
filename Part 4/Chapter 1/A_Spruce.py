def spruce(length) :
    print("a spruce!")
    for i in range(1,length+1,1) :
        print(" " * (length - i), end="")
        print("*" * (2 * i - 1))
    print(" " * (length-2), "*")


while True:
    try:
        number = int(input("what is the length of the spruce(if you want to exit, type negative numbers or zero): "))

        if number <= 0 :
            break

        spruce(number)
    except ValueError :
        print("Please try again.")  