# 7. Показать числа от -N до N

x = int(input('Input any number: '))
numbers = list(range(-x, x+1))
print(*numbers)
