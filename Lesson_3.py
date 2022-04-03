# Дана последовательность чисел.
# Получить список неповторяющихся элементов
# исходной последовательности
# 
# input_list = [3, 5, 6, 8, 9, 5, 6]
# current_list = list(set(input_list))
# print(current_list)

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.


import random


def write_many(k):
    any_list = [random.randint(0, 100) for i in range(k + 1)]
    # print(any_list)
    many_num = ''
    n = k
    for i in range(k + 1):
        if n == 1:
            many_num += str(any_list[i]) + '*x + '
        elif n == 0:
            many_num += str(any_list[i]) + ' = 0'
        else:
            many_num += str(any_list[i]) + f'*x^{n} + '
        n -= 1
    print(many_num)
    data = open('text_for_lesson_3.txt', 'a')
    data.write(many_num + '\n')
    data.close()


def fill_dict(any_list):
    result_dic = {}
    for i in any_list:
        temp_value_1 = ''
        temp_key_1 = ''
        for n in i:
            check = True
            while n.isdigit() and check:
                temp_value_1 += n

            check = False
            while n.isdigit() and not check:
                temp_key_1 += n
            result_dic[temp_key_1] = temp_value_1
    return result_dic


data_1 = open('text_for_lesson_3.txt', 'r')
first_line = data_1.readline()
second_line = data_1.readline()
print(first_line)
print(second_line)
first_temp = first_line.split(' + ')
second_temp = second_line.split(' + ')
print(first_temp)
print(second_temp)
first_dic = fill_dict(first_line)
print(first_dic)

# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найти его. И вставить на нужную позицию.

# data = open('text_for_lesson_3.txt', 'r')
# numbers = data.read().split()
# data.close()
# # numbers = ['1', '2', '4', '5']
# work_list = list(map(int, numbers))
# for i in range(len(work_list) - 1):
#     if work_list[i + 1] - 1 != work_list[i]:
#         work_list.insert(i + 1, work_list[i] + 1)
#         break
# # print(work_list)
# result = ' '.join(map(str, work_list))
# # print(result)
# data = open('text_for_lesson_3.txt', 'w')
# data.write(result)
# data.close()
