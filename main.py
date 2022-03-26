import random

chars = '+-/*!&$#@?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
str = ''
lenght = int(input('How long password you need? '))
c = 0

while c < lenght:
    str += random.choice(chars)
    c += 1

print(str)
