# Показать первую цифру дробной части числа
# a = float(input('Enter any number: '))
# str_a = str(a)
# count = 0
# for i in str_a:
#     count += 1
#     if i == '.':
#         print(str_a[count])

a = float(input('Enter any number: '))
count = int((a * 10) % 10)
print(count)