def add_student(students: dict, name: str):
    key = name.lower()
    students[key] = []

def print_student(students: dict, name: str):
    name_lower = name.lower()
    avg_grade = 0;
    length_credit = 0
    if name_lower in students:
        if students[name_lower]:
            print(f"{name}")
            print(f" {len(students[name_lower])} completed courses:")
            for course, credit in students[name_lower]:
                if credit != 0:
                    print(f"  {course} {credit}")
                    avg_grade += credit
                    length_credit += 1
            print(f" average grade {avg_grade / length_credit}")
        else :
            print(f"{name}:\n no completed courses")
    else:
        print(f"{name}: no such person in the database")
    
def add_course(students: dict, name: str, course: tuple):
    key = name.lower()
    if key in students:
        if course[1] == 0:  
            print(f"{course[0]} dersi kredisi 0 olduğu için eklenemedi.")
            return
       
        existing_course = next((c for c in students[key] if c[0] == course[0]), None)
        
        if existing_course: 
            if existing_course[1] >= course[1]:
                print(f"{course[0]} dersi zaten var ve notu daha yüksek veya eşit.")
            else: 
                students[key].remove(existing_course)
                students[key].append(course)
                print(f"{course[0]} dersinin notu güncellendi.")
        else:
        
            students[key].append(course)
            print(f"{course[0]} dersi eklendi!")
    else:
        print(f"{name}: veritabaninda böyle bir kişi yok")

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")