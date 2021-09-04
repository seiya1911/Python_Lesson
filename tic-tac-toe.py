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
