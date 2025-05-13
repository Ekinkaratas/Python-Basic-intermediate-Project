from random import randint, choice, choices
import string

def generate_strong_password(amount: int, add_number: bool, add_specialchar: bool):
    special_Characters = "!?=+-()#"
    letters = string.ascii_lowercase  # Küçük harfler
    number = "0123456789"  # Sayılar
    password = ""
    password_list = list(letters)  # Harfleri liste olarak ekledik

    # Şifreyi oluştururken küçük harf ekle
    password += choice(letters)  # Rastgele küçük harf
    password_list.extend(list(letters))  # Harfleri password_list'e ekle

    # Sayı eklemek
    if add_number:
        password += choice(number)  # Rastgele bir sayı
        password_list.extend(list(number))  # Sayıları password_list'e ekle

    # Özel karakter eklemek
    if add_specialchar:
        password += choice(special_Characters)  # Rastgele özel karakter
        password_list.extend(list(special_Characters))  # Özel karakterleri password_list'e ekle

    # Şifrenin geri kalan kısmını tamamlamak
    length = amount - len(password)  # Kalan uzunluk
    for _ in range(length):
        password += choice(password_list)  # Rastgele bir karakter seç

    print(password)

# Test örnekleri
print(generate_strong_password(8, True, True))  # Şifre, sayı ve özel karakter içerecek
print(generate_strong_password(8, True, False))  # Şifre, sadece sayı içerecek
print(generate_strong_password(8, False, True))  # Şifre, sadece özel karakter içerecek
print(generate_strong_password(8, False, False))  # Şifre, sadece harf içerecek
