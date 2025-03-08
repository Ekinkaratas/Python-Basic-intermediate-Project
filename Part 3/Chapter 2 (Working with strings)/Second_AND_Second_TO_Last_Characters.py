while True :
    try :
        word = str(input("Please type in string (if you want to exit, type '1'): "))
       
        second_Word = word[1]
        second_TO_last_Characters = word[len(word)-2]

        if word != "1" :
            if second_Word != second_TO_last_Characters:
                print("The second and the second to last characters are different")
            else :
                print(f"The second and the second to last characters are {second_Word}")
        else :
            break
    except ValueError :
        print("Please try again. ")