# Написать калькулятор с операциями: Умножение, деление,
# остаток от деления, вычитание, целочисленное деление.
#
# def calc(a, b, sign):
#     if sign == '+':
#         return a + b
#     elif sign == '-':
#         return a - b
#     elif sign == '*':
#         return a * b
#     elif sign == '/' and b != 0:
#         return a / b
#     elif sign == '//' and b != 0:
#         return a // b
#     elif sign == '%' and b != 0:
#         return a % b
#     else:
#         print('Input error')
#
#
# print(calc(1, 2, '+'))
# print(calc(5, 6, '-'))
# print(calc(5, 6, '*'))
# print(calc(13, 6, '/'))
# print(calc(13, 6, '//'))
# print(calc(13, 6, '%'))
#
#
# # Дана строка текста. Напишите программу для подсчета стоимости строки,
# # исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек.
# # Ответ дайте в рублях и копейках.
#
#
# def calc_value(arg):
#     kop = len(arg) * 60
#     rub = kop // 100
#     kop -= rub * 100
#     value = str(rub) + ' руб. ' + str(kop) + ' коп.'
#     return value
#
#
# n = input('Enter any string:\n')
# print(calc_value(n))


# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних
# пяти цифр на обратный.

# def reverse_number(number):
#     input_string = str(number)
#     if len(input_string) < 5:
#         return 'Input error'
#     new_string = input_string[:-5]
#     end_string = input_string[len(input_string):-6:-1]
#     new_string += end_string
#     return new_string
#
#
# print(reverse_number(1234567))

# n человек, пронумерованных числами от 1 до n
# n, стоят в кругу. Они начинают считаться, каждый
# k-й по счету человек выбывает из круга,
# после чего счет продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека, который
# останется в кругу последним.
#
#
# def counter(n, k):
#     current_list = list(range(1, n + 1))
#     while len(current_list) > 1:
#         current_list.remove(k % len(current_list))
#         print(current_list)
#     return current_list
#
#
# print(counter(4, 2))


# Заданы две клетки шахматной доски. Напишите программу,
# которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES»,
# а если в разные цвета — то «NO».
#
# def chess(x_1, y_1, x_2, y_2):
#     return not (x_1 + y_1 + x_2 + y_2) % 2
#
#
# print(chess(2, 1, 1, 2))

# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате

def check_colours(one_col, sec_col):
    if one_col in base_colours and sec_col in base_colours:
        mix_col = base_colours[one_col] + base_colours[sec_col]
        return mixed_colours[mix_col]
    else:
        return 'Input error.'


base_colours = \
    {
        'red': 'r',
        'blue': 'b',
        'yellow': 'y'
    }
mixed_colours = \
    {
        'rb': 'violet',
        'br': 'violet',
        'ry': 'orange',
        'yr': 'orange',
        'by': 'green',
        'yb': 'green'
    }

current_colours = input('Enter two colours: ')
first_colour, second_colour = current_colours.split()
print(check_colours(first_colour, second_colour))

# На вход программе подается натуральное число n.
# Напишите программу, которая для каждого из чисел от 0 до n (включительно)
# выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
#
# n = 5
# for i in range(n + 1):
#     print('Квадрат числа {} равен {}'.format(i, i ** 2))
