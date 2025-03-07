while True :
    try:
        limit = int(input("Upper limit: "))
        number = 1
        #Cozum 1
        #print(number)
        #number += 1
        #while number < limit : 
        #    print(number)
        #    number += 2
        #break

        #Cozum 2
        while number < limit :
            if number % 2 == 0 or number == 1 :
                print(number)
            number += 1
        break    
    except ValueError:
        print(" Please let the type be Integer. ")