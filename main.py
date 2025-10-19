import random


symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_password = int(input("Длина пароля:"))
password = ""

for i in range(len_password):
    password += random.choice(symbols)
print(password)
