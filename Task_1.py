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