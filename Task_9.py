# 9. Показать последнюю цифру трёхзначного числа

from random import randint
x = randint(100, 1000)
last_number = x % 10
print(f'The last number of {x} is {last_number}')
