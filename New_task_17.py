# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = int(input('Enter N: '))
numbers = {}
if N >= 1:
    for i in range(1, N + 1):
        numbers[i] = 3 * i + 1
    print(numbers)
else:
    print('Input error.')
