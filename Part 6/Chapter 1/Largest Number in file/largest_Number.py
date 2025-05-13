def largest_Number():
    number = 0
    with open("Part 6/Chapter 1/example.txt") as txt:
        for line in txt:
            new_number =  int(line)
            if number < new_number:
                number = new_number
    
    print(f"en buyuk sayi: {number}")

largest_Number()