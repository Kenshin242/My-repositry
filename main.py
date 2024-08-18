import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_len = int(input('Сколько символов пароль: '))

password = ''

for i in range(pass_len):

    password += random.choice(symbols)

print(password)
