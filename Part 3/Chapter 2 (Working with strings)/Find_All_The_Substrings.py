while True:    
    try: 
        word = input("Please type in a word(if you want to exit, type 'exit'): ")
        
        if len(word) <= 2 :
            print("The string must contain more than two characters, please try again.")
            continue
        
        if word.lower() == "exit":
            break  

        character = input("Please type in a character: ")

        if len(character) != 1:
            print("Please enter only one character.")
            continue

        index = word.find(character)

        while index != -1:
            print(word[index:index+3])

            index = word.find(character, index + 1)
    except ValueError :
        print("Please try again. ")