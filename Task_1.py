# Почувствуй себя интерном*

# 0. Вывести квадрат числа
a = int(input('Input a: '))
print(a**2)

# 1. По двум заданным числам проверять является ли первое квадратом второго
a = int(input('Input a: '))
b = int(input('Input b: '))
if b**2 == a:
    print('The first number is the square of the second')
else:
    print('The first number is not the square of the second')

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

# 3. По заданному номеру дня недели вывести его название
# 4. Найти максимальное из трех чисел
# 5. Написать программу вычисления значения функции y = f(a)
# 6. Выяснить является ли число чётным
# 7. Показать числа от -N до N
# 8. Показать четные числа от 1 до N
# 9. Показать последнюю цифру трёхзначного числа
# 10. Показать вторую цифру трёхзначного числа
# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# 12. Удалить вторую цифру трёхзначного числа
# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.
# 14. Найти третью цифру числа или сообщить, что её нет
