# Задания из книги "Грокаем алгоритмы"

# Задача про продавца манго (поиск в ширину)
from collections import deque

graph = {"you": ["alice", "bob", "claire"],
         "bob": ["anuj", "peggy"],
         "alice": ["peggy"],
         "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')
print()


# Задача про графы (алгоритм Дейкстры)


def find_lowest_cost_node(current_costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for current_node in current_costs:  # Перебрать все узлы
        current_cost = current_costs[current_node]
        if current_cost < lowest_cost and current_node not in processed:
            # Если у узла наименьшая стоимость и он еще не был обработан
            lowest_cost = current_cost  # он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = current_node
    return lowest_cost_node


graph = dict()  # Создаем граф
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
    node = find_lowest_cost_node(costs)  # Найти следующий узел с наименьшей стоимостью и повторить цикл

current = 'fin'
solution = ''
while current != 'start':  # Это мой алгоритм для вывода на печать ответа (путь и его стоимость)
    for n in parents.keys():
        if n == current:
            solution = str(parents[current]) + '==>' + str(n) + ' ' + solution
            current = parents[current]
print(f'The way: {solution}')
print(f'The cost is: {costs["fin"]}')
