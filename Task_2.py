# 2. Даны два числа. Показать большее и меньшее число

from random import randint
a = randint(0, 10)
b = randint(0, 10)
print(f'First number is {a}, second number is {b}\n')
if a > b:
    print(f'Greater number is {a}, smaller number is {b}')
elif a == b:
    print(f'The numbers are equal')
else:
    print(f'Greater number is {b}, smaller number is {a}')
