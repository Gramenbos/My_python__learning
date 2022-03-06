# 10. Показать вторую цифру трёхзначного числа

from random import randint
x = randint(100, 999)
second_number = int((x % 100) / 10)
print(f'The second number of {x} is {second_number}')
