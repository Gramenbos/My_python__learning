# Сложите цифры целого числа.
# Решил использовать рекурсию!!!
def sum_numbers(number):
    if number < 10:
        return number
    return number % 10 + sum_numbers(number // 10)


num = int(input('Enter any number: '))
result = sum_numbers(num)
print(f'The sum of the numbers is {result}.')
