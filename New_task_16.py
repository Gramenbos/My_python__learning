# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input('Enter N: '))
numbers = []
current_number = 1
if N >= 1:
    numbers.append(1)
    for i in range(N - 1):
        current_number *= -3
        numbers.append(current_number)
    print(numbers)
else:
    print('Input error.')
