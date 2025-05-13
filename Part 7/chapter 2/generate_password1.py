from random import randint

def generate_password(amount: int):
    return ''.join(chr(randint(ord('a'),ord('z'))) for _ in range(amount))

for i in range(10):
    password = generate_password(8)
    print(password)
