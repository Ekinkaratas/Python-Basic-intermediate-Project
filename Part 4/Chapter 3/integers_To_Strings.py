def formatted ( my_list ) :
    new_list = []
    for var in my_list :
        new_list.append(f"{var:.2f}")

    return new_list

my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)