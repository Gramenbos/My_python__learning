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
    list_in = []
    tmp_str = ''
    for i in range(len(x)):
        if x[i].isdigit():
            tmp_str += x[i]
        else:
            list_in.append(tmp_str)
            tmp_str = ''
            if if_znak(x[i]):
                list_in.append(x[i])
    list_in.append(tmp_str)
    return list_in


def priority(x, a, b):
    for i in range(len(x) - 1):
        if x[i] == a or x[i] == b:
            tmp = calc(int(x[i - 1]), int(x.pop(i + 1)), x.pop(i))
            x[i - 1] = str(tmp)
    return x


numbers = '1+2/2'
work_list = split_numbers(numbers)
print(work_list)
work_list = priority(work_list, '*', '/')
print(work_list)
work_list = priority(work_list, '+', '-')
print(work_list)

# while len(work_list) > 2:
#     if '*' in work_list or '/' in work_list:
#         work_list = priority(work_list, '*', '/')
#         print(work_list)
#     if '+' in work_list or '-' in work_list:
#         work_list = priority(work_list, '*', '/')
#         print(work_list)

# print(priority(work_list, '*', '/'))
#
# print(priority(work_list, '+', '-'))
