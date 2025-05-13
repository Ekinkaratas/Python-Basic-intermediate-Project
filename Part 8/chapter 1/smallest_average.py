def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    def average(Person : dict):
        return (Person["result1"] + Person["result2"] + Person["result3"]) / 3
    
    list_person = [person1,person2,person3]

    return min(list_person, key=average)

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
