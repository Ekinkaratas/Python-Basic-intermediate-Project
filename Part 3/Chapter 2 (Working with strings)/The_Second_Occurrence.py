while True:    
    try: 
        word = input("Please type in a word(if you want to exit, type 'exit'): ")
        if word.lower() == "exit":
            break  

        substring = input("Please type in a substring: ")

        index = word.find(substring)
        if index != -1 :
            index = word.find(substring, index + 1)
            if index != -1 :
                print(f"The second occurrence of the substring is at index {index}")
            else :
                print(f"The substring does not occur twice in the string.")
        else :
            print("no substring to create!")
    except ValueError :
        print("Please try again. ")