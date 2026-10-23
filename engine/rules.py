from engine.board import board, column_number
from engine.moves import (
    pawn_moves,
    knight_moves,
    bishop_moves,
    rook_moves,
    queen_moves,
    king_moves,
    get_moves_for_piece,
)


def is_square_safe(index):
    if 0<board[index]<8:
            for i in range(64):
                piece_value = board[i]
                if piece_value >8:
                    if piece_value == 10:
                        possible_moves = pawn_moves(i)
                    elif piece_value ==11:
                        possible_moves = knight_moves(i)
                    elif piece_value ==12:  
                        possible_moves = bishop_moves(i)
                    elif piece_value ==13:
                        possible_moves = rook_moves(i)
                    elif piece_value ==14:
                        possible_moves = queen_moves(i)
                    elif piece_value ==9:
                        white_king_index = i
                        kings_vicinity = [white_king_index-8,white_king_index+8,white_king_index+1,white_king_index-1,white_king_index+9,white_king_index-9,white_king_index-7,white_king_index+7]
                        j = 0
                        while j < len(kings_vicinity):
                            if kings_vicinity[j] < 0 or kings_vicinity[j]>63:
                                kings_vicinity.remove(kings_vicinity[j])
                            else:
                                j+=1
                        k = 0
                        while k < len(kings_vicinity):
                            final_kings_position = column_number(kings_vicinity[k])
                            initial_kings_position = column_number(white_king_index)
                            if abs(final_kings_position - initial_kings_position) > 1:
                                kings_vicinity.remove(kings_vicinity[k])
                            else:
                                k+=1
                        possible_moves = kings_vicinity

                    if index in possible_moves:
                        return False
            return True
    elif 8<board[index]<16:
            for i in range(64):
                piece_value = board[i]
                if 0<piece_value<8:
                    if piece_value == 2: 
                        possible_moves = pawn_moves(i)
                    elif piece_value ==3:
                        possible_moves = knight_moves(i)
                    elif piece_value ==4:
                        possible_moves = bishop_moves(i)
                    elif piece_value ==5:
                        possible_moves = rook_moves(i)
                    elif piece_value ==6:
                        possible_moves = queen_moves(i)
                    elif piece_value ==1:
                        black_king_index = i
                        kings_vicinity = [black_king_index-8,black_king_index+8,black_king_index+1,black_king_index-1,black_king_index+9,black_king_index-9,black_king_index-7,black_king_index+7]
                        j = 0
                        while j < len(kings_vicinity):
                            if kings_vicinity[j] < 0 or kings_vicinity[j]>63:
                                kings_vicinity.remove(kings_vicinity[j])
                            else:
                                j+=1
                        k = 0
                        while k < len(kings_vicinity):
                            final_kings_position = column_number(kings_vicinity[k])
                            initial_kings_position = column_number(black_king_index)
                            if abs(final_kings_position - initial_kings_position) > 1:
                                kings_vicinity.remove(kings_vicinity[k])
                            else:
                                k+=1
                        possible_moves = kings_vicinity
                    if index in possible_moves:
                        return False
            return True
    return True


def is_legal(index,target):
    piece_value = board[index]
    original_piece = board[index]
    final_piece = board[target]
    board[target] = original_piece
    board[index] =0
    for i in range(64):
        if piece_value<8:
            if board[i]==1:
                king_index = i
                if is_square_safe(king_index)== False:
                    board[index] = original_piece
                    board[target] = final_piece
                    return False
        elif piece_value>8:
            if board[i]==9:
                king_index = i
                if is_square_safe(king_index)== False:
                    board[index] = original_piece
                    board[target] = final_piece
                    return False
                
    board[index] = original_piece
    board[target] = final_piece
    return True

def is_checkmate(index):
    piece_value = board[index]
    if piece_value == 1:
        if is_square_safe(index) == False and len(king_moves(index))==0:
            # the king is in threat and has no legal moves
            for i in range(64):
                piece = board[i]
                if 0<piece<8:
                    if piece == 2:
                        possible_moves = pawn_moves(i)
                    elif piece ==3:
                        possible_moves = knight_moves(i)    
                    elif piece ==4:
                        possible_moves = bishop_moves(i)
                    elif piece ==5:
                        possible_moves = rook_moves(i)
                    elif piece ==6:
                        possible_moves = queen_moves(i) 
                    for move in possible_moves:
                        target_piece = board[move]
                        board[move] = piece
                        board[i] = 0
                        if is_square_safe(index) == True:
                            board[i] = piece
                            board[move] = target_piece
                            return False
                        board[i] = piece
                        board[move] = target_piece
            return True
    elif piece_value == 9:
        if is_square_safe(index) == False and len(king_moves(index))==0:
            # the king is in threat and has no legal moves
            for i in range(64):
                piece = board[i]
                if 8<piece<16:
                    if piece == 10:
                        possible_moves = pawn_moves(i)
                    elif piece ==11:
                        possible_moves = knight_moves(i)    
                    elif piece ==12:
                        possible_moves = bishop_moves(i)
                    elif piece ==13:
                        possible_moves = rook_moves(i)
                    elif piece ==14:
                        possible_moves = queen_moves(i) 
                    for move in possible_moves:
                        target_piece = board[move]
                        board[move] = piece
                        board[i] = 0
                        if is_square_safe(index) == True:
                            board[i] = piece
                            board[move] = target_piece
                            return False
                        board[i] = piece
                        board[move] = target_piece
            return True

def check_and_promote(target_index):
    piece_value = board[target_index]
    if piece_value == 10 and target_index < 8:
        board[target_index] = 14 
        print("White Pawn promoted to Queen!")
    elif piece_value == 2 and target_index > 55:
        board[target_index] = 6  
        print("Black Pawn promoted to Queen!")
        
def get_all_moves(color):
    position = []
    if color == "white":
        for i in range(64):
            piece = board[i]
            if 8<piece<16:
                possible_moves = get_moves_for_piece(i,piece)
                if len(possible_moves)>0:
                    for move in possible_moves:
                        if is_legal(i,move):
                            position.append((i,move))
    elif color == "black":
        for i in range(64):
            piece = board[i]
            if 0<piece<8:
                possible_moves = get_moves_for_piece(i,piece)
                if len(possible_moves)>0:
                    for move in possible_moves:
                        if is_legal(i,move):
                            position.append((i,move))
    return position
