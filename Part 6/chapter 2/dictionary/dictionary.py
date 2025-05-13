# this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block. 

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    
    try:
        selection = int(input("Function: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if selection == 1 :
        try:
         map = {}
         key = str(input(("The word in Turkish: ")))
         map[key] = str(input(("The word in English: ")))

         with open("dictionary.txt","a") as file:
             file.write(f"{key} : {map[key]}\n")

        except FileNotFoundError:
            print("Diary file not found. Add an entry first.\n")
    
    elif selection == 2 :
        search = str(input(("Search term: ")))
        control_Flag = False
        try:
            with open("dictionary.txt","r") as file:
                for line in file:
                    parts = line.strip().split(":") # strip() sag ve soldaki bosluklari sildi, skplit(":") ise ":" gore bolup liste seklinde geri dondurdu
                    if search in parts[0] or search in parts[1]:
                        if len(parts) == 2:  # güvenlik: iki parça mı diye bak
                            turkish = parts[0].strip()
                            english = parts[1].strip()
                            print(f"{turkish} - {english}")
                        control_Flag = True    
                if not control_Flag:
                    print(f"there is nothing about {search}.\n")
        except FileNotFoundError:
            print("Diary file not found. Add an entry first.\n")
    
    elif selection == 3:
        print("Goodbye!")
        break

    else:
        print("Invalid selection. Please choose 0, 1, or 2.\n")   


