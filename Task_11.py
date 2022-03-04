# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

from random import randint
x = randint(10, 99)
first_number = int(x / 10)
second_number = x % 10
if first_number >= second_number:
    print(f'The largest digit of {x} is {first_number}.')
else:
    print(f'The largest digit of {x} is {second_number}.')
