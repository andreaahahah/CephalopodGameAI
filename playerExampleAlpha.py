import playingStrategies



#usiamo un cutoff dinamico
def playerStrategy(game, state):
    quante = quanteCelle(state)
    if (quante > 20):
        cutOff = 5
    else:
        if (quante > 17):
            cutOff = 4
        else:
            cutOff = 3
    value, move = playingStrategies.h_alphabeta_search(game, state, playingStrategies.cutoff_depth(cutOff))
    return move


def quanteCelle(board):
    quante = 0
    size = len(board.board)
    for r in range(size):
        for c in range(size):
            if board.board[r][c] is None:
                continue
            quante += 1
    return quante
# TODO forse è utile aumentare il cutOff quando ci avviciniamo alla fine
