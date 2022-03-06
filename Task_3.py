# 3. По заданному номеру дня недели вывести его название

week_days_list = ['Monday', 'Tuesday', 'Wednesday',
                  'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day = int(input('Input number of day of the week: ')) - 1
if 0 <= current_day <= 6:
    print('Current day is {}.'.format(week_days_list[current_day]))
else:
    print('Input error.')
