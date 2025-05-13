while True:
    print("1 - Add an entry, 2 - Read entries, 0 - Quit")
    try:
        selection = int(input("Function: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if selection == 1:
        text = input("Diary entry: ")
        with open("Part 6/Chapter 1/Diary_save_txt/diary.txt", "a") as file:
            file.write(text + "\n")
        print("Diary saved.\n")

    elif selection == 2:
        try:
            with open("Part 6/Chapter 1/Diary_save_txt/diary.txt", "r") as file:
                entries = file.readlines()
                if entries:
                    print("\nDiary entries:")
                    for line in entries:
                        print(line.strip())
                else:
                    print("Diary is empty.\n")
        except FileNotFoundError:
            print("Diary file not found. Add an entry first.\n")

    elif selection == 0:
        print("Goodbye!")
        break

    else:
        print("Invalid selection. Please choose 0, 1, or 2.\n")

