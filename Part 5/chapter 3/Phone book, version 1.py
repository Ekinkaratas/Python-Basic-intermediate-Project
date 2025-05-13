def search(name: str):
    if name in phone_book:
        print(f"phone number : {phone_book[name]}")
    else:
        print("no number")

def add(name : str, number: str):
    if name in phone_book:
        if phone_book[name] != number:
            print(f"Name already exists with a different number ({phone_book[name]}).")
            update = input("Do you want to update it? (y/n): ").lower()
            if update == "y":
                phone_book[name] = number
                print("Number updated!")
            else:
                print("Number not updated.")
        else:
            print("Name and number already exist.")
    else:
        phone_book[name] = number
        print("Ok!")



if __name__ == "__main__" :
    phone_book = {}
    while True:
        try:
            selection = int(input("command (1 search, 2 add, 3 quit): "))
        except ValueError:
            print("please, type in integer")
            continue

        if selection == 1:
            try:
                name = str(input("Name: "))
            except ValueError:
                print("please, type in string")
                continue

            search(name)

        elif selection ==2:
            try:
                name = str(input("Name: "))
                phone_number = str(input("Number: "))
            except ValueError:
                print("please, type in string and number")
                continue
            add(name,phone_number)
        elif selection == 3:
            print("quitting...")
            break