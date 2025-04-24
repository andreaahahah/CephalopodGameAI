import math

from CephalopodGame import get_subsets

inizio_io = True
controllato = False
def minimax_search(game, state):
    """Search game tree to determine best move; return (value, move) pair."""

    player = state.to_move
    def max_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a))
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(state):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a))
            if v2 < v:
                v, move = v2, a
        return v, move

    return max_value(state)

infinity = math.inf

def alphabeta_search(game, state):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move

    def max_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    def min_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity)



def cache1(function):
    "Like lru_cache(None), but only considers the first argument of function."
    cache = {}
    def wrapped(x, *args):
        if x not in cache:
            cache[x] = function(x, *args)
        return cache[x]
    return wrapped


def alphabeta_search_tt(game, state):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move

    @cache1
    def max_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    @cache1
    def min_value(state, alpha, beta):
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity)

def cutoff_depth(d):
    """A cutoff function that searches to depth d."""
    return lambda game, state, depth: depth > d

def h_alphabeta_search(game, state, cutoff=cutoff_depth(2)):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move
    

    @cache1
    def max_value(state, alpha, beta, depth):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if cutoff(game, state, depth):
            return h(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta, depth+1)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    @cache1
    def min_value(state, alpha, beta, depth):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if cutoff(game, state, depth):
            return h(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta, depth + 1)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity, 0)


def h1_alphabeta_search(game, state, cutoff=cutoff_depth(2)):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = state.to_move
    

    @cache1
    def max_value(state, alpha, beta, depth):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if cutoff(game, state, depth):
            return h1(state, player), None
        v, move = -infinity, None
        for a in game.actions(state):
            v2, _ = min_value(game.result(state, a), alpha, beta, depth+1)
            if v2 > v:
                v, move = v2, a
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move

    @cache1
    def min_value(state, alpha, beta, depth):
        if game.is_terminal(state):
            return game.utility(state, player), None
        if cutoff(game, state, depth):
            return h1(state, player), None
        v, move = +infinity, None
        for a in game.actions(state):
            v2, _ = max_value(game.result(state, a), alpha, beta, depth + 1)
            if v2 < v:
                v, move = v2, a
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move

    return max_value(state, -infinity, +infinity, 0)

'''def h (board, player):
    avversario = 0
    io = 0
    size = len(board.board)
    for r in range(size):
        for c in range(size):
            if board.board[r][c] is None:
                continue
            cell = board.board[r][c]
            giocatore, pip = cell
            if giocatore == player:
                # allora sto parlando di me
                io += 1
                if pip == 6:
                    io += 3
            else:
                avversario += 1
                if pip == 6:
                    avversario += 3
    return io - avversario'''


def h(board, player):
    avversario = 0
    io = 0
    size = len(board.board)
    center = size // 2

    global controllato
    if not controllato:
        chi_inizia(board, player)
        controllato = True

    for r in range(size):
        for c in range(size):
            if board.board[r][c] is None:
                continue
            cell = board.board[r][c]
            giocatore, pip = cell
            distance_to_center = max(abs(r - center), abs(c - center))

            if giocatore == player:
                # allora sto parlando di me
                io += 1
                io += assess_vulnerability(board, r, c) * -1
                if pip == 6:
                    io += 6
                if pip >= 4:
                    io += 3
            else:
                avversario += 1
                avversario += assess_vulnerability(board, r, c) * -1
                if pip == 6:
                    avversario += 8
                if pip >= 4:
                    avversario += 1

            if distance_to_center == 0:
                # Cella centrale
                if giocatore == player:
                    io += 4
                else:
                    avversario += 4

            if distance_to_center == 1:
                # Cella centrale
                if giocatore == player:
                    io += 1
                else:
                    avversario += 1

            if giocatore != player and pip == 1 and inizio_io:
                io += 2

    return io - avversario


def h1(board, player):
    avversario = 0
    io = 0
    size = len(board.board)
    center = size // 2

    for r in range(size):
        for c in range(size):
            if board.board[r][c] is None:
                continue
            cell = board.board[r][c]
            giocatore, pip = cell
            distance_to_center = max(abs(r - center), abs(c - center))

            if giocatore == player:
                # allora sto parlando di me
                io += 1
                io += assess_vulnerability(board, r, c) * -1
                if pip == 6:
                    io += 6
                if pip >=4:
                    io+=3
            else:
                avversario += 1
                avversario += assess_vulnerability(board, r, c) * -1
                if pip == 6:
                    avversario += 8
                if pip >=4:
                    avversario+=1

            if distance_to_center == 0 :
                # Cella centrale
                if giocatore == player:
                    io += 4
                else:
                    avversario += 4

            if distance_to_center == 1 :
                # Cella centrale
                if giocatore == player:
                    io += 1
                else:
                    avversario += 1


    return io - avversario

#con questi pesi riesce a vincere con se stesso con i pesi diversi
def assess_vulnerability(board, r, c):
    """Valuta quanto è vulnerabile una cella alla cattura"""
    size = len(board.board)
    vulnerability = 0

    # Controlla le celle adiacenti vuote
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < size and 0 <= nc < size and board.board[nr][nc] is None:
            # Controlla le altre celle adiacenti a questa cella vuota
            adjacent_pips = []
            for dr2, dc2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr2, nc2 = nr + dr2, nc + dc2
                if 0 <= nr2 < size and 0 <= nc2 < size and board.board[nr2][nc2] is not None:
                    if (nr2, nc2) != (r, c):  # Non includere la cella che stiamo valutando
                        adjacent_pips.append(board.board[nr2][nc2][1])

            # Aggiungi il pip della cella corrente
            current_pip = board.board[r][c][1]

            # Controlla combinazioni di celle che potrebbero portare a cattura
            for i in range(1, len(adjacent_pips) + 1):
                for subset in get_subsets(adjacent_pips, i):
                    total = sum(subset) + current_pip
                    if 2 <= total <= 6:
                        vulnerability += 1  # Aumenta vulnerabilità

    return vulnerability
#aggiungere il controllo della vulnerabilità dei dadi, e forzare l'euristica sul centro, dando valori più elevati più si è vicini al centro
            

def chi_inizia(board, player):
    avversario = 0
    io = 0
    size = len(board.board)
    for r in range(size):
        for c in range(size):
            if board.board[r][c] is None:
                continue
            cell = board.board[r][c]
            giocatore, pip = cell
            if giocatore == player:
                io += 1
            else:
                avversario += 1
    if avversario > io:
        global inizio_io
        inizio_io = False
        global controllato
        controllato = True

