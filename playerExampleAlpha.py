import playingStrategies



def playerStrategy(game, state):
    quante = quanteCelle(state)
    if (quante > 20):
        cutOff = 5
    else:
        if (quante > 15):
            cutOff = 4
        else:
            cutOff = 3  # The depth of the search tree. It can be changed to test the performance of the player.
    # The player uses the alphabeta search algorithm to find the best move.
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
