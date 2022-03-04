# 14. Найти третью цифру числа или сообщить, что её нет

number = input('Enter any number, please: ')
if len(number) >= 3:
    print(f'The third digit of the number is {number[2]}.')
else:
    print('There is not a third digit in the number.')
