from engine.board import board
from engine.tables import (
    mg_pawn_table, eg_pawn_table,
    mg_knight_table, eg_knight_table,
    mg_bishop_table, eg_bishop_table,
    mg_rook_table, eg_rook_table,
    mg_queen_table, eg_queen_table,
    mg_king_table, eg_king_table,
)


def get_phase():
    queen = 0
    for i in range(64):
        piece = board[i]
        if piece == 6 or piece ==14:
            queen +=1
    if queen ==0:
        return "endgame"
    else:
        return "midgame"

def midgame_evaluation():
    mg_value = [0, 82, 337, 365, 477, 1025, 12000]
    mg_score = 0
    for i in range(64):
        piece = board[i]
        if piece == 0:
            continue
        if piece == 2:  
                mg_score -= mg_value[1] + mg_pawn_table[56^i]
        elif piece ==3:
                mg_score -= mg_value[2] + mg_knight_table[56^i]
        elif piece ==4:
                mg_score -= mg_value[3] + mg_bishop_table[56^i]
        elif piece ==5:
                mg_score -= mg_value[4] + mg_rook_table[56^i]
        elif piece ==6:
                mg_score -= mg_value[5] + mg_queen_table[56^i]
        elif piece ==1:
                mg_score -= mg_value[6] + mg_king_table[56^i]
        elif piece ==10:
                mg_score += mg_value[1] + mg_pawn_table[i]
        elif piece ==11:
                mg_score += mg_value[2] + mg_knight_table[i]
        elif piece ==12:
                mg_score += mg_value[3] + mg_bishop_table[i]
        elif piece ==13:
                mg_score += mg_value[4] + mg_rook_table[i]
        elif piece ==14:
                mg_score += mg_value[5] + mg_queen_table[i]
        elif piece ==9:
                mg_score += mg_value[6] + mg_king_table[i]
    return mg_score

def endgame_evaluation():
    eg_value = [0, 94, 281, 297, 512,  936, 12000]
    eg_score = 0
    for i in range(64):
        piece = board[i]
        if piece == 0:
            continue
        if piece == 2:  
                eg_score -= eg_value[1] + eg_pawn_table[56^i]
        elif piece ==3:
                eg_score -= eg_value[2] + eg_knight_table[56^i]
        elif piece ==4:
                eg_score -= eg_value[3] + eg_bishop_table[56^i]
        elif piece ==5:
                eg_score -= eg_value[4] + eg_rook_table[56^i]
        elif piece ==6:
                eg_score -= eg_value[5] + eg_queen_table[56^i]
        elif piece ==1:
                eg_score -= eg_value[6] + eg_king_table[56^i]
        elif piece ==10:
                eg_score += eg_value[1] + eg_pawn_table[i]
        elif piece ==11:
                eg_score += eg_value[2] + eg_knight_table[i]
        elif piece ==12:
                eg_score += eg_value[3] + eg_bishop_table[i]
        elif piece ==13:
                eg_score += eg_value[4] + eg_rook_table[i]
        elif piece ==14:
                eg_score += eg_value[5] + eg_queen_table[i]
        elif piece ==9:
                eg_score += eg_value[6] + eg_king_table[i]
    return eg_score 

def evaluate_board():
    phase = get_phase()
    
    if phase == "midgame":
        return midgame_evaluation()
    else:
        return endgame_evaluation()
