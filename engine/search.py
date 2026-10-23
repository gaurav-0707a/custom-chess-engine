"""Move search: minimax (no alpha-beta pruning yet)."""

from engine.board import board
from engine.rules import get_all_moves
from engine.evaluation import evaluate_board


def best_move_at_depth1(color):
    change_in_evaluation = []
    all_moves = get_all_moves(color)
    if len(all_moves) == 0:
        return None
    # this was not something i thought , possibility of no moves being available at a moment
    for move in all_moves:
        piece = board[move[0]]
        target_piece = board[move[1]]
        board[move[1]] = piece
        board[move[0]] = 0
        final_points = evaluate_board()
        change_in_evaluation.append(final_points)
        board[move[0]] = piece
        board[move[1]] = target_piece
    if color == "white":
        best_move_possible = max(change_in_evaluation)
    else:
        best_move_possible = min(change_in_evaluation)  
    indices = change_in_evaluation.index(best_move_possible)
    return all_moves[indices]  


# refer to sebastian lague tutorial on minimax algorithms and alpha beta pruning for better understanding
def minimax(position, depth , maximizingPlayer):
    if depth == 0:
        return evaluate_board()
    
    if maximizingPlayer:
        maxEval = -float('inf')
        all_moves = get_all_moves("white")
        for move in all_moves:
            piece = board[move[0]]
            target_piece = board[move[1]]
            board[move[1]] = piece
            board[move[0]] = 0
            eval = minimax(position, depth-1 , False)
            maxEval = max(maxEval , eval)
            board[move[0]] = piece
            board[move[1]] = target_piece
        return maxEval
    else:
        minEval = float('inf')
        all_moves = get_all_moves("black")
        for move in all_moves:
            piece = board[move[0]]
            target_piece = board[move[1]]
            board[move[1]] = piece
            board[move[0]] = 0
            eval = minimax(position, depth-1 , True)
            minEval = min(minEval , eval)
            board[move[0]] = piece
            board[move[1]] = target_piece
        return minEval

def get_best_move(depth, color):
    best_move = None
    
    if color == "white":
        maxEval = -float('inf')
        all_moves = get_all_moves("white")
        for move in all_moves:
            piece = board[move[0]]
            target_piece = board[move[1]]
            board[move[1]] = piece
            board[move[0]] = 0
            eval = minimax(None, depth - 1, False)
            board[move[0]] = piece
            board[move[1]] = target_piece
            
            if eval > maxEval:
                maxEval = eval
                best_move = move
                
    else: 
        minEval = float('inf')
        all_moves = get_all_moves("black")
        for move in all_moves:

            piece = board[move[0]]
            target_piece = board[move[1]]
            board[move[1]] = piece
            board[move[0]] = 0

            eval = minimax(None, depth - 1, True)

            board[move[0]] = piece
            board[move[1]] = target_piece
            
            if eval < minEval:
                minEval = eval
                best_move = move
                
    return best_move
