# Подсчитать сумму цифр в вещественном числе.

a = float(input())
h = str(a)
count = 0
for i in h:
    if i != '.':
        count += int(i)
print(count)
