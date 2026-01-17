board = [0]*64
piece_map = {
    'k': 1, 'q': 6, 'r': 5, 'b': 4, 'n': 3, 'p': 2,  # Black
    'K': 9, 'Q': 14, 'R': 13, 'B': 12, 'N': 11, 'P': 10 # White 
}
print("paste the FEN string of the position:")
fen_string = str(input())
piece_wise_column = fen_string.split("/")
for row in range(8):
    row_string = piece_wise_column[row]
    current_col = 0
    for char in row_string:
        if char.isdigit():
            skip_count = int(char)
            current_col += skip_count
        else:
            square_index = (row * 8) + current_col
            board[square_index] = piece_map[char]
            current_col += 1
# pesto tables now
game_phase_inc = {
    1: 0, 2: 1, 3: 1, 4: 2, 5: 4, 6: 0,  # White (P, N, B, R, Q, K)
    9: 0, 10: 1, 11: 1, 12: 2, 13: 4, 14: 0  # Black
}

# --- PeSTO Piece Values (Base Material) ---
mg_value = [0, 82, 337, 365, 477, 1025, 12000]
eg_value = [0, 94, 281, 297, 512,  936, 12000]


mg_pawn_table = [
    0,   0,   0,   0,   0,   0,   0,   0,
    98, 134,  61,  95,  68, 126,  34, -11,
    -6,   7,  26,  31,  65,  56,  25, -20,
    -14,  13,   6,  21,  23,  12,  17, -23,
    -27,  -2,  -5,  12,  17,   6,  10, -25,
    -26,  -4,  -4, -10,   3,   3,  33, -12,
    -35,  -1, -20, -23, -15,  24,  38, -22,
    0,   0,   0,   0,   0,   0,   0,   0,
]

eg_pawn_table = [
    0,   0,   0,   0,   0,   0,   0,   0,
    178, 173, 158, 134, 147, 132, 165, 187,
    94, 100,  85,  67,  56,  53,  82,  84,
    32,  24,  13,   5,  -2,   4,  17,  17,
    13,   9,  -3,  -7,  -7,  -8,   3,  -1,
    4,   7,  -6,   1,   0,  -5,  -1,  -8,
    13,   8,   8,  10,  13,   0,   2,  -7,
    0,   0,   0,   0,   0,   0,   0,   0,
]

mg_knight_table = [
    -167, -89, -34, -49,  61, -97, -15, -107,
    -73, -41,  72,  36,  23,  62,   7,  -17,
    -47,  60,  37,  65,  84, 129,  73,   44,
    -9,  17,  19,  53,  37,  69,  18,   22,
    -13,   4,  16,  13,  28,  19,  21,   -8,
    -23,  -9,  12,  10,  19,  17,  25,  -16,
    -29, -53, -12,  -3,  -1,  18, -14,  -19,
    -105, -21, -58, -33, -17, -28, -19,  -23,
]

eg_knight_table = [
    -58, -38, -13, -28, -31, -27, -63, -99,
    -25,  -8, -25,  -2,  -9, -25, -24, -52,
    -24, -20,  10,   9,  -1,  -9, -19, -41,
    -17,   3,  22,  22,  22,  11,   8, -18,
    -18,  -6,  16,  25,  16,  17,   4, -18,
    -23,  -3,  -1,  15,  10,  -3, -20, -22,
    -42, -20, -10,  -5,  -2, -20, -23, -44,
    -29, -51, -23, -15, -22, -18, -50, -64,
]


mg_bishop_table = [
    -29,   4, -82, -37, -25, -42,   7,  -8,
    -26,  16, -18, -13,  30,  59,  18, -47,
    -16,  37,  43,  40,  35,  50,  37,  -2,
    -4,   5,  19,  50,  37,  37,   7,  -2,
    -6,  13,  13,  26,  34,  12,  10,   4,
    0,  15,  15,  15,  14,  27,  18,  10,
    4,  15,  16,   0,   7,  21,  33,   1,
    -33,  -3, -14, -21, -13, -12, -39, -21,
]

eg_bishop_table = [
    -14, -21, -11,  -8, -7,  -9, -17, -24,
    -8,  -4,   7, -12, -3, -13,  -4, -14,
    -4,   8,   4, -21, -21, -13,  -7, -12,
    -6,  -7,   6,  19,  21, -5,   1, -11,
    -5,  -1,  12,  14,  11,  1,   3, -10,
    -3,   5,   7,   6,   4,  9,  -2,  -9,
    -10, -11,   0,  -5,  -3,  1,  -3,  -5,
    -23, -10,  -4,   2,   2,  3, -13, -11,
]
mg_rook_table = [
    32,  42,  32,  51, 63,  9,  31,  43,
    27,  32,  58,  62, 80, 67,  26,  44,
    -5,  19,  26,  36, 17, 45,  61,  16,
    -24, -11,   7,  26, 24, 35,  -8, -20,
    -36, -26, -12,  -1,  9, -7,   6, -23,
    -45, -25, -16, -17,  3,  0,  -5, -33,
    -44, -16, -20,  -9, -1, 11,  -6, -71,
    -19, -13,   1,  17, 16,  7, -37, -26,
]
eg_rook_table = [
    13,  10,  18,  15, 12,  12,   8,   5,
    11,  13,  13,  11, -3,   3,   8,   3,
    7,   7,   7,   5,  4,  -3,  -5,  -3,
    4,   3,  13,   1,  2,   1,  -1,   2,
    3,   5,   8,   4, -5,  -6,  -8, -11,
    -4,   0,  -5,  -1, -7, -12,  -8, -16,
    -6,  -6,   0,   2, -9,  -9, -11,  -3,
    -9,   2,   3,  -1, -5, -13,   4, -20,
]
mg_queen_table = [
    -28,   0,  29,  12,  59,  44,  43,  45,
    -24, -39,  -5,   1, -16,  57,  28,  54,
    -13, -17,   7,   8,  29,  56,  47,  57,
    -27, -27, -16, -16,  -1,  17,  -2,   1,
    -9, -26, -9, -10,  -2,  -4,   3,  -3,
    -14,   2, -11,  -2,  -5,   2,  14,   5,
    -35,  -8,  11,   2,   8,  15,  -3,   1,
    -1, -18,  -9,  10, -15, -25, -31, -50,
]
eg_queen_table = [
    -9,  22,  22,  27,  27,  19,  10,  20,
    -17,  20,  32,  41,  58,  25,  30,   0,
    -20,   6,   9,  49,  47,  35,  19,   9,
    3,  22,  24,  45,  57,  40,  57,  36,
    -18,  28,  19,  47,  31,  34,  39,  23,
    -16, -27,  15,   6,   9,  17,  10,   5,
    -22, -23, -30, -16, -16, -23, -36, -32,
    -33, -28, -22, -43,  -5, -32, -20, -41,
]
mg_king_table = [
    -65,  23,  16, -15, -56, -34,   2,  13,
    29,  -1, -20,  -7,  -8,  -4, -38, -29,
    -9,  24,   2, -16, -20,   6,  22, -22,
    -17, -20, -12, -27, -30, -25, -14, -36,
    -49,  -1, -27, -39, -46, -44, -33, -51,
    -14, -14, -22, -46, -44, -30, -15, -27,
    1,   7,  -8, -64, -43, -16,   9,   8,
    -15,  36,  12, -54,   8, -28,  24,  14,
]
eg_king_table = [
    -74, -35, -18, -18, -11,  15,   4, -17,
    -12,  17,  14,  17,  17,  38,  23,  11,
    10,  17,  23,  15,  20,  45,  44,  13,
    -8,  22,  24,  27,  26,  33,  26,   3,
    -18,  -4,  21,  24,  27,  23,   9, -11,
    -19,  -3,  11,  21,  23,  16,   7,  -9,
    -27, -11,   4,  13,  14,   4,  -5, -17,
    -53, -34, -21, -11, -28, -14, -24, -43,
]
def column_number(index):
    return index%8

def row_number(index):
    return index//8

def is_enemy(index,target):
    if 0<board[index]<8 and board[target]>8:
        return True
    elif 8<board[index]<16 and 0<board[target]<8:
        return True
    else:
        return False
    
def notations(row,column):
    position = 8*(row) + column
    return position
    

def knight_moves(index):
    knight_possibility = [index-17,index-15,index-10,index-6,index+6,index+10,index+15,index+17]
    knight = 0
    knights = 0
    while knight < (len(knight_possibility)):
        if knight_possibility[knight] > 63 or knight_possibility[knight] < 0:
            knight_possibility.remove(knight_possibility[knight])
        else:
            knight+=1
    # print(knight_possibility)
    while knights <(len(knight_possibility)):
        if board[knight_possibility[knights]] > 0:
            if is_enemy(index,knight_possibility[knights])== False:
                knight_possibility.remove(knight_possibility[knights])
            else:
                knights+=1
        else:
            knights+=1
    def column_of_knight(index):
        return index % 8
    initial_knight_column = column_of_knight(index)
    knight_jump = 0
    while knight_jump < len(knight_possibility):
        final_knight_column = column_of_knight(knight_possibility[knight_jump])
        if abs(final_knight_column - initial_knight_column) > 2:
            knight_possibility.remove(knight_possibility[knight_jump])
        else:
            knight_jump+=1
    return knight_possibility

def king_moves(index):
    kings_possibility = [index-8,index+8,index+1,index-1,index+9,index-9,index-7,index+7]
    king = 0
    kings = 0
    king_jumps = 0
    while kings < len(kings_possibility):
        if kings_possibility[kings] < 0 or kings_possibility[kings]>63:
            kings_possibility.remove(kings_possibility[kings])
        else:
            kings+=1
    while king < len(kings_possibility):
        if board[kings_possibility[king]]>0:
            if is_enemy(index,kings_possibility[king])== False:
                kings_possibility.remove(kings_possibility[king])
            else:
                king +=1
        else:
            king +=1
    while king_jumps < len(kings_possibility):
        final_kings_position = column_number(kings_possibility[king_jumps])
        initial_kings_position = column_number(index)
        if abs(final_kings_position - initial_kings_position) > 1:
            kings_possibility.remove(kings_possibility[king_jumps])
        else:
            king_jumps +=1
    return kings_possibility

def pawn_moves(index):
    pawn_value = board[index]
    if pawn_value == 10:
        pawn = 0
        pawns = 0
        if 48<=index<55:
            pawn_possibility = [index-8,index-16]
        else:
            pawn_possibility= [index - 8]
        while pawns < len(pawn_possibility):
            if pawn_possibility[pawns]>63 or pawn_possibility[pawns] < 0:
                pawn_possibility.remove(pawn_possibility[pawns])
            else:
                pawns+=1
        while pawn<len(pawn_possibility):
            target = pawn_possibility[pawn]
            if board[pawn_possibility[pawn]] > 0:
                if target == index - 8:
                    pawn_possibility = []
                    break
                else:
                    pawn_possibility.remove(target)
            else:
                pawn +=1
        target_left = index - 9
        if target_left >= 0 and column_number(index) > 0:
            if board[target_left] > 0 and is_enemy(index, target_left):
                pawn_possibility.append(target_left)

        target_right = index - 7
        if target_right >= 0 and column_number(index) < 7:
            if board[target_right] > 0 and is_enemy(index, target_right):
                pawn_possibility.append(target_right)
    elif pawn_value == 2:
        pawn = 0
        pawns = 0
        if 8<=index<=15:
            pawn_possibility = [index+8,index+16]
        else:
            pawn_possibility= [index + 8]
        while pawns < len(pawn_possibility):
            if pawn_possibility[pawns]>63 or pawn_possibility[pawns] < 0:
                pawn_possibility.remove(pawn_possibility[pawns])
            else:
                pawns+=1
        while pawn<len(pawn_possibility):
            target = pawn_possibility[pawn]
            if board[pawn_possibility[pawn]] > 0:
                if target == index+8:
                    pawn_possibility = []
                    break
                else:
                    pawn_possibility.remove(target)  
            else:
                pawn +=1
        target_left = index + 7
        if target_left <= 63 and column_number(index) > 0:
            if board[target_left] > 0 and is_enemy(index, target_left):
                pawn_possibility.append(target_left)
        target_right = index + 9
        if target_right <= 63 and column_number(index) < 7:
            if board[target_right] > 0 and is_enemy(index, target_right):
                pawn_possibility.append(target_right)
    return pawn_possibility

def rook_moves(index):
    rook_possibility = []
    # 1) GOING RIGHT
    target1 = index + 1
    while target1 < 64 and board[target1]==0:
        rook_possibility.append(target1)
        target1 = target1 + 1
    initial_rook_row = row_number(index)
    rook1 = 0 
    while rook1 < len(rook_possibility):
        final_rook_row = (rook_possibility[rook1])//8
        if abs(initial_rook_row - final_rook_row) != 0:
            rook_possibility.remove(rook_possibility[rook1])
        else:
            rook1+=1
    # 2)Going left
    target2 = index - 1
    while target2>=0 and board[target2]==0:
        rook_possibility.append(target2)
        target2 = target2 - 1
    rook2 = 0 
    while rook2 < len(rook_possibility):
        final_rook_row = (rook_possibility[rook2])//8
        if abs(initial_rook_row - final_rook_row) != 0:
            rook_possibility.remove(rook_possibility[rook2])
        else:
            rook2+=1
    #3)Going up
    target3 = index -8
    while target3 >=0 and board[target3]==0:
        rook_possibility.append(target3)
        target3 = target3 - 8
    #4)Going down
    target4 = index + 8
    while target4<64 and board[target4]==0:
        rook_possibility.append(target4)
        target4 = target4 +8
    # target1 = target1 +1
    if 0<=target1<64 and row_number(target1)== row_number(index) and is_enemy(index,target1)== True:
        rook_possibility.append(target1)
    # target2 = target2 -1
    if 0<=target2<64 and row_number(target2)== row_number(index) and is_enemy(index,target2)== True:
        rook_possibility.append(target2)
    # target3 = target3 -8
    if 0<=target3<64 and is_enemy(index,target3)== True:
        rook_possibility.append(target3)
    # target4 = target4 +8
    if 0<=target4<64 and is_enemy(index,target4)== True:
        rook_possibility.append(target4)
    return rook_possibility

def bishop_moves(index):
    bishop_possibility = []
    target1 = index + 7
    while target1<64 and board[target1]== 0:
        if abs(target1 % 8 - (target1 - 7) % 8) > 1:
            break #this if block is gemini'ed
        bishop_possibility.append(target1)
        target1 = target1 + 7
    target2 = index - 7
    while target2>=0 and board[target2]==0:
        if abs(target2 % 8 - (target2 + 7) % 8) > 1:
            break
        bishop_possibility.append(target2)
        target2 = target2 - 7
    target3 = index - 9
    while target3>=0 and board[target3]==0:
        if abs(target3 % 8 - (target3 +9) % 8) > 1:
            break
        bishop_possibility.append(target3)
        target3 = target3 - 9
    target4 = index + 9
    while target4<64 and board[target4]==0:
        if abs(target4 % 8 - (target4 - 9) % 8) > 1:
            break
        bishop_possibility.append(target4)
        target4 = target4 + 9
    if 0<=target1<64:
        prev_square = target1 - 7
        if abs(column_number(target1) - column_number(prev_square)) <= 1 and is_enemy(index,target1)== True:
            bishop_possibility.append(target1)  
    if 0<=target2<64:
        prev_square = target2 + 7
        if abs(column_number(target2) - column_number(prev_square)) <= 1 and is_enemy(index,target2)== True:
            bishop_possibility.append(target2)
    if 0<=target3<64:
        prev_square = target3 + 9
        if abs(column_number(target3) - column_number(prev_square)) <= 1 and is_enemy(index,target3)== True:
            bishop_possibility.append(target3)
    if 0<=target4<64:
        prev_square = target4 - 9
        if abs(column_number(target4) - column_number(prev_square)) <= 1 and is_enemy(index,target4)== True:
            bishop_possibility.append(target4)
    return bishop_possibility

def queen_moves(index):
    straight_moves = rook_moves(index)
    diagonal_moves = bishop_moves(index)
    queen_possibility = straight_moves + diagonal_moves
    return queen_possibility


def get_moves_for_piece(idx, val):
    if val == 10 or val == 2: return pawn_moves(idx)
    if val == 11 or val == 3: return knight_moves(idx)
    if val == 12 or val == 4: return bishop_moves(idx)
    if val == 13 or val == 5: return rook_moves(idx)
    if val == 14 or val == 6: return queen_moves(idx)
    if val == 9 or val == 1: return king_moves(idx)
    return []


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


# gemini'd this part to call the function , mera ghee khatam hai
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

#  yea this part is ai as well for now

piece_presentation = {
    1: 'k', 6:'q', 5:'r', 4:'b', 3:'n', 2:'p',  # Black
    9:'K', 14:'Q', 13:'R', 12:'B', 11:'N', 10:'P' # White 
}

def print_board():
    for row in range(8):
        for column in range(8):
            index = notations(row,column)
            piece = board[index]
            if piece == 0:
                print('.', end=' ')
            else:
                print(piece_presentation[piece], end=' ')
        print()

# --- MAIN EXECUTION ---

# 1. Ask for Depth (Difficulty)
try:
    print("\n--- CHESS ENGINE SETTINGS (No Pruning) ---")
    print("Depth 1: Instant")
    print("Depth 2: Fast (~1-2 secs)")
    print("Depth 3: Slow (~30-60 secs)")
    depth_input = int(input("Select AI Depth: "))
    if depth_input < 1: depth_input = 1
except ValueError:
    print("Invalid input. Defaulting to Depth 2.")
    depth_input = 2

print_board()

moves = 0
while moves < 1000: 
    turn_is_white = (moves % 2 == 0)

    king_index = -1
    target_king = 9 if turn_is_white else 1
    for i in range(64):
        if board[i] == target_king:
            king_index = i
            break

    if king_index == -1: break

    if is_checkmate(king_index):
        print("\n" + "="*20)
        print("CHECKMATE!")
        print("Black wins!" if turn_is_white else "White wins!")
        print("="*20)
        break

    print("\n" + ("White's turn (Human)" if turn_is_white else "Black's turn (AI)"))
    if turn_is_white:
        valid_move_made = False
        while not valid_move_made:
            try:
                index = int(input("Input the index of the piece you want to move: "))
                if index < 0 or index > 63: 
                    print("Index out of bounds.")
                    continue
                    
                piece_value = board[index]
                
                if piece_value < 9:
                    print("Illegal: Pick a White piece.")
                    continue

                possible_destinations = get_moves_for_piece(index, piece_value)

                if not possible_destinations:
                    print("That piece has no physical moves. Pick another.")
                    continue

                print("Physical moves available:", possible_destinations)
                target = int(input("Enter target index: "))
                
                if target in possible_destinations and is_legal(index, target):
                    board[target] = board[index]
                    board[index] = 0
                    check_and_promote(target) 
                    
                    print_board()
                    valid_move_made = True
                    moves += 1
                else:
                    print("Illegal Move! (King in danger or blocked).")
                    
            except (ValueError, IndexError):
                print("Error: Enter a valid number 0-63.")


    else:
        print(f"AI is thinking at Depth {depth_input}...")

        best_move = get_best_move(depth_input, "black")
        
        if best_move is None:
            print("Stalemate or Checkmate. AI Resigns.")
            break
        start, end = best_move
        print(f"AI moves from {start} to {end}")
        
        board[end] = board[start]
        board[start] = 0
        check_and_promote(end) 
        
        print_board()
        moves += 1