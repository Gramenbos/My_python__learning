# Определить, присутствует ли в заданном списке строк,
# некоторое число


def check_str(any_number, any_list):
    for i in any_list:
        return any_number in i


current_list = ['123', 'adfr45', '768123fyk']
number = int(input('Enter number: '))
number_str = str(number)
print(check_str(number_str, current_list))
