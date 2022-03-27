# Найти сумму чисел списка стоящих на нечетной позиции

work_list = [2, 4, 5, 6, 7, 214]
count = 0
for i in range(1, len(work_list), 2):
    count += work_list[i]
print(count)
