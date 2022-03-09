# Сообщить, в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
X = int(input('Enter X: '))
Y = int(input('Enter Y: '))
if X == 0 and Y != 0:
    print('The point is on the Y-axis')
elif X != 0 and Y == 0:
    print('The point is on the X-axis')
elif X > 0 and Y > 0:
    print('The point is in the first quarter')
elif X < 0 and Y > 0:
    print('The point is in the second quarter')
elif X < 0 and Y < 0:
    print('The point is in the third quarter')
elif X > 0 and Y < 0:
    print('The point is in the forth quarter')
else:
    print('The point is at the intersection of the X and Y axes')
