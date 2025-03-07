while True :
    try:
        limit = int(input("Upper limit: "))
        number = 1
        while number < limit : 
            print(number)
            number += 1
        break
    except ValueError:
        print(" Please let the type be Integer. ")