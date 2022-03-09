# Найти расстояние между двумя точками пространства
import math

X_1, Y_1 = map(int, input('Enter coordinates of the first point (X, Y): ').split(','))
X_2, Y_2 = map(int, input('Enter coordinates of the second point (X, Y): ').split(','))
distance = math.sqrt((X_1 - X_2) ** 2 + (Y_1 - Y_2) ** 2)
print(f'Distance is {distance:.{2}f}.')  # Здесь :.{2}f используется, чтобы вывести только 2 знака после запятой
