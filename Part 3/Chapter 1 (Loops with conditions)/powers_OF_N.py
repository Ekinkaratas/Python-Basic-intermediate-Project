while True:
    try:
        limit = int(input("Upper Limit: ")) 
        Base = int(input("Base: "))  

        if Base <= 1:
            print("Base should be greater than 1!")
            continue

        number = 1

        while number < limit:
            print(number)
            number *= Base 

        break

    except ValueError:
        print("Please let the type be Integer")
