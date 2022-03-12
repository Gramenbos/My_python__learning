# Задания из книги "Грокаем алгоритмы"
# Сортировка
from collections import deque


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def sum_numbers(number):
    if number < 10:
        return number
    return number % 10 + sum_numbers(number // 10)


def sum_numbers_in_arr(arr):
    if len(arr) < 1:
        return 0
    return int(arr[0]) + int(sum_numbers_in_arr(arr[1:]))


print(selection_sort([5, 3, 6, 2, 10, -10, 123]))
num = int(input('Enter any number: '))
array = str(num)
print(f'The sum of the numbers (in array) is {sum_numbers_in_arr(array)}.')
print(f'The sum of the numbers (in number) is {sum_numbers(num)}.')


# Задача про хэш-таблицы
# voted = {}
#
#
# def check_voter(name):
#     if voted.get(name):
#         print('Kick them out!')
#     else:
#         voted[name] = True
#         print('Let them vote!')
#
#
# check_voter('Tom')
# check_voter('Mike')
# check_voter('Mike')

# Задача про продавца манго
# graph = {"you": ["alice", "bob", "claire"],
#          "bob": ["anuj", "peggy"],
#          "alice": ["peggy"],
#          "claire": ["thom", "jonny"],
#          "anuj": [], "peggy": [], "thom": [], "jonny": []}
#
#
# def person_is_seller(name):
#     return name[-1] == 'm'
#
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print(person + ' is a mango seller')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
#
# search('you')

# Задача про графы (алгоритм Дейкстры)


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # Если у узла наименьшая стоимость и он еще не был обработан
            lowest_cost = cost  # он назначается нвоым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


graph = {}  # Создаем граф
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
infinity = float('inf')  # Переменная со значением бесконечность
costs = {'a': 6, 'b': 2, 'fin': infinity}  # Хэш-таблица стоимости
parents = {'a': "start", 'b': "start", 'fin': None}  # Хэш-таблица родителей
processed = []  # Список для хранения проверенных узлов
node = find_lowest_cost_node(costs)
while node is not None:  # Если обработаны все узлы, цикл завершится
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебрать вех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # Если к соседу можно добраться быстрее через текущий узел, то:
            costs[n] = new_cost  # обновить стоимость этого узла
            parents[n] = node  # узел становится новым родителем для соседа
    processed.append(node)  # узел добавляется в список обработанных
    node = find_lowest_cost_node(costs)  # Найти следующий узел  с наименьшей стоиомстью и посторить цикл

current = 'fin'
solution = ''
while current != 'start':  # Это мой алгоритм для вывода на печать ответа (путь и его стоимость)
    for n in parents.keys():
        if n == current:
            solution = str(parents[current]) + '==>' + str(n) + ' ' + solution
            current = parents[current]
print(f'The way: {solution}')
print(f'The cost is: {costs["fin"]}')
