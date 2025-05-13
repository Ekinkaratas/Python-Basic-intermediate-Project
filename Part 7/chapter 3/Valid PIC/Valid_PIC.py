def is_it_valid(pic: str):
    if len(pic) == 11:
        control_character = "0123456789ABCDEFHJKLMNPRSTUVWXY"

        birthOfDate = pic[0:6]
        Just_Year = pic[4:6]
        year = ""
        
        marker_For_Century_Flag = pic[6]
        if marker_For_Century_Flag == "+" :
            year += f"18{Just_Year}"
        elif marker_For_Century_Flag == "-" :
            year += f"19{Just_Year}"
        elif marker_For_Century_Flag == "A" :
            year += f"20{Just_Year}"
        else :
            return print("Invalid century!!!")
        
        control_character_number = (int (f"{birthOfDate}{pic[7:10]}")) % 31

        return True if pic[10] == control_character[control_character_number] else print("Invalid PIC number")           
   
    return print("PIC number less than 11 letters ")

if is_it_valid("120488+246L") :
    print("Valid PIC number")


    



