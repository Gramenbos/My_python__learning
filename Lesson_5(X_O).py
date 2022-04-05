def draw_board(current_board):
    print("-" * 13)
    for i in range(3):
        print("|", current_board[0 + i * 3], "|", current_board[1 + i * 3], "|", current_board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        if not player_answer.isdigit():
            print('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        player_answer = int(player_answer)
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in 'XO':
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(current_board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if current_board[each[0]] == current_board[each[1]] == current_board[each[2]]:
            return current_board[each[0]]
    return False


def main(current_board):
    counter = 0
    while counter < 9:
        draw_board(current_board)
        if not counter % 2:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            winner = check_win(current_board)
            if winner:
                draw_board(current_board)
                print(winner, "выиграл!")
                break
    if counter == 9:
        draw_board(current_board)
        print("Ничья!")


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
board = list(range(1, 10))
main(board)
