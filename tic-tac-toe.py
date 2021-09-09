'三目並べのプログラムです'
OPEN = 0
FIRST = 1
SECOND = 2
EVEN = 3

turn = 1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

log1 = [[0, 0], [1, 1], [1, 0], [2, 0], [0, 2],
        [0, 1], [2, 1], [2, 2], [1, 2], [EVEN]]
log2 = [[0, 0], [1, 0], [1, 1], [2, 2], [0, 1],
        [2, 0], [FIRST]]
log3 = [[0, 1], [0, 0], [2, 1], [1, 1], [2, 2],
        [2, 0], [1, 0], [0, 2], [SECOND]]


def show_turn():
    '手番を示す文字列を返す'
    if turn == FIRST:
        return('先手')
    elif turn == SECOND:
        return('後手')
    else:
        return('手番の値が不適切です')


def init_turn():
    '手番を初期化する'
    global turn
    turn = 1


def change_turn():
    '手番を交代する'
    global turn
    if turn == FIRST:
        turn = SECOND
    elif turn == SECOND:
        turn = FIRST


def test_turn():
    '手番をテストする'
    init_turn()
    print(show_turn(), 'の番です')
    change_turn()
    print(show_turn(), 'の番です')
    change_turn()
    print(show_turn(), 'の番です')


def show_board():
    '盤面を表す文字列を返す'
    s = ' :0 1 2\n---------\n'
    for i in range(3):
        s = s + str(i) + ':'
        for j in range(3):
            cell = ''
            if board[i][j] == OPEN:
                cell = ' '
            elif board[i][j] == FIRST:
                cell = '0'
            elif board[i][j] == SECOND:
                cell = 'X'
            else:
                cell = '?'
            s = s + cell + ' '
        s = s + '\n'
    return s


def init_board():
    '盤面すべて空（OPEN）に初期化する'
    for i in range(3):
        for j in range(3):
            board[i][j] = OPEN


def examine_board(i, j):
    '盤面の i , j の位置の値を返す'
    return board[i][j]


def set_board(i, j, t):
    if (i >= 0) and (i < 3) and (j >= 0) and (j < 3):
        if (t > 0) and (t < 3):
            if examine_board(i, j) == 0:
                board[i][j] = t
                return 'OK'
            else:
                return 'Not empty'
        else:
            return 'illegal turn'
    else:
        return 'illegal slot'


def test_board1():
    init_board()
    print(show_board())
    print(set_board(0, 0, 1))
    print(show_board())
    print(set_board(1, 1, 2))
    print(show_board())
    print(set_board(1, 1, 1))
    print(show_board())


def check_board_horizontal(t):
    for i in range(3):
        if (board[i][0] == t) and (board[i][1] == t) and (board[i][2] == t):
            return True
    return False


def check_board_vertical(t):
    for j in range(3):
        if (board[0][j] == t) and (board[1][j] == t) and (board[2][j] == t):
            return True
    return False


def check_board_diagonal(t):
    if (board[0][2] == t) and (board[1][1] == t) and (board[2][0] == t):
        return True
    return False


def check_board_inverse_diagonal(t):
    if (board[0][2] == t) and (board[1][1] == t) and (board[2][0] == t):
        return True
    return False


def is_win_simple(t):
    if check_board_horizonal(t):
        return True
    if check_board_vertical(t):
        return True
    if check_board_diagonal(t):
        return True
    if check_board_inverse_diagonal(t):
        return True
    return False


def is_win_actual(t):
    if not is_win_simple(t):
        return False
    if t == FIRST:
        if is_win_simple(SECOND):
            return False
    else:
        if is_win_simple(FIRST):
            return False
    return True


def is_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == OPEN:
                return False
    return True


def is_even():
    if is_win_simple(FIRST):
        return False
    if is_win_simple(SECOND):
        return False
    if not is_full():
        return False
    return True


def test_board2():
    init_board()
    board[0][0] = FIRST
    board[1][0] = FIRST
    board[2][0] = FIRST
    print(show_board())
    print('HORIZONTAL FIRST: ', check_board_horizontal(FIRST))
    print('HORIZONTAL SECOND: ', check_board_horizontal(SECOND))
    print('VERTICAL FIRST: ', check_board_vertical(FIRST))
    print('VERTICAL SECOND: ', check_board_vertical(SECOND))
    init_board()
    board[0][0] = SECOND
    board[1][0] = SECOND
    board[2][0] = SECOND
    print(show_board())
    print('HORIZONTAL FIRST: ', check_board_horizontal(FIRST))
    print('HORIZONTAL SECOND: ', check_board_horizontal(SECOND))
    print('VERTICAL FIRST: ', check_board_vertical(FIRST))
    print('VERTICAL SECOND: ', check_board_vertical(SECOND))
    init_board()
    board[0][0] = FIRST
    board[0][1] = FIRST
    board[0][2] = FIRST
    print(show_board())
    print('HORIZONTAL FIRST: ', check_board_horizontal(FIRST))
    print('HORIZONTAL SECOND: ', check_board_horizontal(SECOND))
    print('VERTICAL FIRST: ', check_board_vertical(FIRST))
    print('VERTICAL SECOND: ', check_board_vertical(SECOND))
    init_board()
    board[0][0] = SECOND
    board[0][1] = SECOND
    board[0][2] = SECOND
    print(show_board())
    print('HORIZONTAL FIRST: ', check_board_horizontal(FIRST))
    print('HORIZONTAL SECOND: ', check_board_horizontal(SECOND))
    print('VERTICAL FIRST: ', check_board_vertical(FIRST))
    print('VERTICAL SECOND: ', check_board_vertical(SECOND))
    init_board()
    board[0][0] = FIRST
    board[1][1] = FIRST
    board[2][2] = FIRST
    print(show_board())
    print('DIAGONAL FIRST: ', check_board_diagonal(FIRST))
    print('DIAGONAL SECOND: ', check_board_diagonal(SECOND))
    print('INV DIAGONAL FIRST: ', check_board_inverse_diagonal(FIRST))
    print('INV DIAGONAL SECOND: ', check_board_inverse_diagonal(SECOND))
    init_board()
    board[0][0] = SECOND
    board[1][1] = SECOND
    board[2][2] = SECOND
    print(show_board())
    print('DIAGONAL FIRST: ', check_board_diagonal(FIRST))
    print('DIAGONAL SECOND: ', check_board_diagonal(SECOND))
    print('INV DIAGONAL FIRST: ', check_board_inverse_diagonal(FIRST))
    print('INV DIAGONAL SECOND: ', check_board_inverse_diagonal(SECOND))
    init_board()
    board[0][2] = FIRST
    board[1][1] = FIRST
    board[2][0] = FIRST
    print(show_board())
    print('DIAGONAL FIRST: ', check_board_diagonal(FIRST))
    print('DIAGONAL SECOND: ', check_board_diagonal(SECOND))
    print('INV DIAGONAL FIRST: ', check_board_inverse_diagonal(FIRST))
    print('INV DIAGONAL SECOND: ', check_board_inverse_diagonal(SECOND))
    init_board()
    board[0][2] = SECOND
    board[1][1] = SECOND
    board[2][0] = SECOND
    print(show_board())
    print('DIAGONAL FIRST: ', check_board_diagonal(FIRST))
    print('DIAGONAL SECOND: ', check_board_diagonal(SECOND))
    print('INV DIAGONAL FIRST: ', check_board_inverse_diagonal(FIRST))
    print('INV DIAGONAL SECOND: ', check_board_inverse_diagonal(SECOND))


def test_board3():
  init_board()
  board[0][0] = FIRST
  


def replay_log(log):
    init_board()
    init_turn()
    print(show_board())
    for m in log:
        if len(m) == 2:
            print(show_turn(), 'の番です')
            print(set_board(m[0], m[1], turn))
            print(show_board())
            print('IS WIN', turn, ':', is_win_actual(turn))
            change_turn()
        else:
            print('RESULT IN LOG: ', m[0])
        print('IS WIN FIRST: ', is_win_actual(FIRST))
        print('IS WIN SECOND: ', is_win_actual(SECOND))
        print('IS EVEN: ', is_even())


def test_log():
    print('LOG1')
    replay_log(log1)
    print('LOG2')
    replay_log(log2)
    print('LOG3')
    replay_log(log3)


def test_all():
    test_turn()
    test_board1()
    test_board2()
    test_board3()
    test_log()
