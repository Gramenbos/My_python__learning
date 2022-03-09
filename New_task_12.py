# При заданном целом числе n посчитайте n + nn + nnn.
number = input('Enter any number: ')
double_num = int(number * 2)
triple_num = int(number * 3)
num = int(number)
result = num + double_num + triple_num
print(result)
