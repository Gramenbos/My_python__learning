# Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти
quarter_index = int(input('Enter quarter index (1-4): '))
if quarter_index == 1:
    print('Valid values are: X > 0, Y > 0')
elif quarter_index == 2:
    print('Valid values are: X < 0, Y > 0')
elif quarter_index == 3:
    print('Valid values are: X < 0, Y < 0')
elif quarter_index == 4:
    print('Valid values are: X > 0, Y < 0')
else:
    print('Input error')
