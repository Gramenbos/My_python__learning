# Написать программу преобразования десятичного числа в двоичное

number = int(input('Enter number: '))
current_list = []
while number > 0:
    current_list.append(str(number % 2))
    number //= 2
print(''.join(current_list[::-1]))
