# 4. Найти максимальное из трех чисел

from random import randint
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c
print(f'Maximum number from {a}, {b}, {c} is {max_number}.')
