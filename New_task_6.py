# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
week_days_list = ['Monday', 'Tuesday', 'Wednesday',
                  'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day = int(input('Input number of day of the week: ')) - 1
if 0 <= current_day <= 6:
    print('Current day is {}.'.format(week_days_list[current_day]))
    if current_day > 4:
        print('It is weekend!')
    else:
        print('It is not weekend.')
else:
    print('Input error.')