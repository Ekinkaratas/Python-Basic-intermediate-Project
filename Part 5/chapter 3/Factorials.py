import math

def factorials(n: int) -> dict:
    return {num: math.factorial(num) for num in range(1,n+1)}


k = factorials(5)
print(k[1])
print(k[3])
print(k[5])