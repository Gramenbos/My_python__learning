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
voted = {}


def check_voter(name):
    if voted.get(name):
        print('Kick them out!')
    else:
        voted[name] = True
        print('Let them vote!')


check_voter('Tom')
check_voter('Mike')
check_voter('Mike')

# Задача про продавца манго
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
