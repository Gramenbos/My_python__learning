# Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой

first_string = input('Enter first string: ')
second_string = input('Enter second string: ')
count = 0
i = 0
while i < len(first_string):
    for j in range(len(second_string)):
        if i < len(first_string):
            if first_string[i] == second_string[j]:
                if j == len(second_string) - 1:
                    count += 1
            i += 1

print(count)

# Есть специальный метод:
print(first_string.count(second_string))
