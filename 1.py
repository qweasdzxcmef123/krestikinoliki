# игровое поле
board = [[" " for _ in range(3)] for _ in range(3)]


# отображение игрового поля
def display_board():
    for row in board:
        print("|".join(row))
        print("-----")


# функция для проверки победы
def check_win(player):
    # проверяем строки
    for row in board:
        if all(cell == player for cell in row):
            return True

    # проверяем столбцы
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# основной игровой цикл
def play_game():
    current_player = "X"
    game_over = False

    while not game_over:
        display_board()
        row = int(input("Выберите строку (0-2): "))
        col = int(input("Выберите столбец (0-2): "))

        # проверяем, что выбранная ячейка пуста
        if board[row][col] == " ":
            board[row][col] = current_player

            # проверяем победу текущего игрока
            if check_win(current_player):
                display_board()
                print("Игрок", current_player, "победил!")
                game_over = True
            # Проверяем ничью
            elif all(cell != " " f  or row in board for cell in row):
                display_board()
                print("Ничья!")
                game_over = True
            # Переключаем игрока
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Выбранная ячейка уже занята. Попробуйте снова.")

play_game()