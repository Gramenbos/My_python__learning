from emoji import emojize


def draw_candies(count):
    print('Осталось ' + str(count) + ' конфет.')
    candy = emojize(':candy:') + ' '
    while count > 10:
        print(candy * 10)
        count -= 10
    print(candy * count)


def take_input(player_num, min_num, max_num, num_of_cand):
    while True:
        player_answer = input('Игрок ' + str(player_num) + ', сколько конфет возьмешь? ')
        if not player_answer.isdigit():
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        player_answer = int(player_answer)
        if min_num <= player_answer <= max_num:
            if player_answer <= num_of_cand:
                return player_answer
            else:
                print('Осталось меньше конфет, чем ты хочешь взять!')
                continue
        else:
            print('Некорректный ввод. Введите число от {} до {}.'.format(min_num, max_num))


def main(number_of_candies):
    draw_candies(number_of_candies)
    minimum_take = 1
    maximum_take = 3
    move = 1
    while number_of_candies > 0:
        if move:
            player_take = take_input(1, minimum_take, maximum_take, number_of_candies)
            number_of_candies -= player_take
            if number_of_candies == 0:
                print('\nПобедил игрок 1 ' + emojize(':1st_place_medal:'))
                break
            draw_candies(number_of_candies)
            move = 0
        else:
            player_take = take_input(2, minimum_take, maximum_take, number_of_candies)
            number_of_candies -= player_take
            if number_of_candies == 0:
                print('\nПобедил игрок 2 ' + emojize(':1st_place_medal:'))
                break
            draw_candies(number_of_candies)
            move = 1


main(10)
