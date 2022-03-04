# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

first_number = int(input('Enter first number: '))
second_number = int(
    input('Enter the second number to check the multiplicity of the first: '))
modulo = second_number % first_number
if modulo == 0:
    print('The second number is a multiple of the first.')
else:
    print(f'The second number isn\'t a multiple of the first. The modulo is: {modulo}')
