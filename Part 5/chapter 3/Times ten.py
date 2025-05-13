def times_ten(start_index: int, end_index: int) -> dict:
    return {i : i*10 for i in range(start_index, end_index+1)}
    

d = times_ten(3, 6)
print(d)