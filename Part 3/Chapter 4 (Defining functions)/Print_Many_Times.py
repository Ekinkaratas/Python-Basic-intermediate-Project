def print_many_times(text,number) :
    for i in range(number) :
        print(text)


while True :
    try:
        text = str(input("Please type in a text or word(if you want to exit, type '1'): "))
        
        if text == '1' :
            break
        
        times = int(input("how many times to repeat: "))

        print_many_times(text,times)

    except ValueError:
        print("Please try again.")