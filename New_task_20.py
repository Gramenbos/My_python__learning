# Написать программу получающую набор произведений
# чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

result = []
n = int(input())
temp = 1
for i in range(1, n + 1):
    temp *= i
    result.append(temp)
print(result)
