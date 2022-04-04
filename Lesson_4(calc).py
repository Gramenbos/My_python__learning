# Напишите программу, удаляющую из текста все слова содержащие "абв".

# any_str = 'Если б мишабвки были пчелабвами 123.'
# del_str = 'абв'
# tmp = any_str.split()
# res = list(filter(lambda item: del_str not in item, tmp))
# res = ' '.join(res)
# print(res)

# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок,
# меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

def calc(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/' and b != 0:
        return int(a / b)
    elif sign == '//' and b != 0:
        return a // b
    elif sign == '%' and b != 0:
        return a % b
    else:
        print('Input error')


def if_znak(s):
    return s in ['+', '-', '*', '/', '(', ')']


def split_numbers(x):
    x.replace(' ', '')
    add_num = []
    tmp_num = ''
    for i in range(len(x)):
        if x[i].isdigit():
            tmp_num += x[i]
            if i == len(x) - 1:
                add_num.append(int(tmp_num))
        else:
            if x[i - 1].isdigit():
                if tmp_num != '':
                    add_num.append(int(tmp_num))
                tmp_num = ''
            if if_znak(x[i]):
                add_num.append(x[i])
    return add_num


def operation(x, a, b):
    for i in range(len(x) - 1):
        if x[i] == a or x[i] == b:
            tmp = calc(x[i - 1], x[i + 1], x[i])
            x[i - 1] = tmp
            x.pop(i + 1)
            x.pop(i)
            return x
    # return x


def calc_all(numb_list):
    while '*' in numb_list or '/' in numb_list:
        numb_list = operation(numb_list, '*', '/')
    while '+' in numb_list or '-' in numb_list:
        numb_list = operation(numb_list, '+', '-')
    return numb_list


def calc_parentheses(num_list):
    if '(' in num_list and ')' in num_list:
        for i in range(len(num_list)):
            if num_list[i] == '(':
                first_num = i
            if num_list[i] == ')':
                second_num = i
                first_list = num_list[:first_num]
                second_list = calc_all(num_list[first_num + 1: second_num])
                third_list = num_list[second_num + 1:]
                num_list = first_list + second_list + third_list
                break
    return num_list


def super_calc(num_list):
    while '(' in num_list and ')' in num_list:
        num_list = calc_parentheses(num_list)
    num_list = calc_all(num_list)
    return num_list


numbers = '5*(5+4)+6*(4+1*(55-5))'
work_list = split_numbers(numbers)
# print(work_list)
work_list = super_calc(work_list)
# print(work_list)
print('{} = {}'.format(numbers, *work_list))
