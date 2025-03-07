while True :
    try:
        limit = int(input("Upper Limit: "))

        number = 2
        total = 1
        text = "The consecutive sum: 1 "

        while total < limit :
            total += number
            text += f"+ {number} "
            number += 1
            
        
        print(f"{text} = {total}")

    except ValueError :
        print("Please let the type be Integer")