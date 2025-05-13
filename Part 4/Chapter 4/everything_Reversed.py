def everything_reversed ( my_list ) :
    new_list = []
    for var in my_list :
        new_list.append(var[::-1])
    
    reversed_NewList = []
    for i in range(len(new_list)-1,-1,-1) :
        reversed_NewList.append(new_list[i])

    return reversed_NewList

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
