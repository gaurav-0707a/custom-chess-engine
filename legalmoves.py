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
# print(board)
N, S, E, W = -8, 8, 1, -1
NE, NW, SE, SW = -7, -9, 9, 7

# Mapping pieces to their movement directions
move_offsets = {
    'n': [-17, -15, -10, -6, 6, 10, 15, 17], 
    'N': [-17, -15, -10, -6, 6, 10, 15, 17], 
    
    'b': [NE, NW, SE, SW], 
    'B': [NE, NW, SE, SW],
    
    'r': [N, S, E, W],   
    'R': [N, S, E, W],
    
    'q': [N, S, E, W, NE, NW, SE, SW], 
    'Q': [N, S, E, W, NE, NW, SE, SW],
    
    'k': [N, S, E, W, NE, NW, SE, SW], 
    'K': [N, S, E, W, NE, NW, SE, SW]
}

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
    
# i am now defining legal moves for each piece tho it doesnt account for checks , castling , en passant and promotion yet , will add them after creating a baby level game 
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
# Code for capturing pieces now! , done


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
# Code for capturing pieces now , done

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
    return pawn_possibility
# code for captures!


# using ray tracing for rooks and bishops coz it has a cool name
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
# Code for capture now! , done


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
# capturing code is already done in rook and bishop functions

def notations(row,column):
    position = 8*(row) + column
    return position

# creating the board now
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
# print_board()


# had to gemini this part as i was unsure about the input loop functioning correctly
moves = 0
while moves < 100:  # Game can last longer than 64 moves
    print_board()
    turn_is_white = (moves % 2 == 0)
    print("White's turn" if turn_is_white else "Black's turn")
    
    # --- START OF DEBUGGED INPUT LOOP ---
    valid_move_made = False
    while not valid_move_made:
        print("Input the index of the piece you want to move:")
        try:
            index = int(input())
            piece_value = board[index]
            
            # Validation: Ensure they pick their own piece
            if turn_is_white and piece_value < 9:
                print("Illegal: You must pick a White piece (K, Q, R, B, N, P).")
                continue
            if not turn_is_white and (piece_value > 8 or piece_value == 0):
                print("Illegal: You must pick a Black piece (k, q, r, b, n, p).")
                continue

            # Your existing logic to fetch possible_destinations
            if piece_value == 2 or piece_value == 10:
                possible_destinations = pawn_moves(index)
            elif piece_value == 3 or piece_value == 11:
                possible_destinations = knight_moves(index)
            elif piece_value == 4 or piece_value == 12:
                possible_destinations = bishop_moves(index)
            elif piece_value == 5 or piece_value == 13:
                possible_destinations = rook_moves(index)
            elif piece_value == 6 or piece_value == 14:
                possible_destinations = queen_moves(index)
            elif piece_value == 1 or piece_value == 9:
                possible_destinations = king_moves(index)

            print("Legal moves for the piece at index", index, "are:", possible_destinations)
            
            if not possible_destinations:
                print("That piece has no legal moves. Pick another one.")
                continue

            target = int(input("Enter where you want to move: "))
            
            if target in possible_destinations:
                # Execute the move
                board[target] = board[index]
                board[index] = 0
                valid_move_made = True  # This breaks the inner loop
                moves += 1              # Only increment turn here
            else:
                print("Illegal move! That index is not in the possible moves list. Try again.")
                
        except (ValueError, IndexError):
            print("Error: Please enter a valid index between 0 and 63.")


# writing logic for pawn promotion , castle , en passant , pins , check and checkmate now!!

# 1) Pawn Promotion
# def pawn_promotion(index):
#     pawn_value = board[index]
#     if pawn_value == 2:
#         possible_moves = pawn_moves(index)
#         for move in possible_moves:
#             if 56<=move<=63:
#                 board[index] = 0
#                 board[move] = 6 #promoting to queen directly fn
#     elif pawn_value == 10:
#         possible_moves = pawn_moves(index)
#         for move in possible_moves:
#             if 0<=move<=7:
#                 board[index] = 0
#                 board[move] = 14 #promoting to queen directly fn

def check_and_promote(target_index):
    piece_value = board[target_index]
    if piece_value == 10 and target_index < 8:
        board[target_index] = 14  # Change to White Queen
        print("White Pawn promoted to Queen!")
    elif piece_value == 2 and target_index > 55:
        board[target_index] = 6   # Change to Black Queen
        print("Black Pawn promoted to Queen!")
                
    # elif pawn_value == 10:
    #     possible_moves = pawn_moves(index)
    #     for move in possible_moves:
    #         if 0<=move<=7:
    #             arsenal.extend([11,12,13,14])
    # return arsenal

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
    last_check = 0
    while last_check< len(kings_possibility):
        if is_square_safe(kings_possibility[last_check]) == False:
            kings_possibility.remove(kings_possibility[last_check])
        else:
            last_check +=1
       
    return kings_possibility



def get_moves_for_piece(idx, val):
    if val == 10 or val == 2: return pawn_moves(idx)
    if val == 11 or val == 3: return knight_moves(idx)
    if val == 12 or val == 4: return bishop_moves(idx)
    if val == 13 or val == 5: return rook_moves(idx)
    if val == 14 or val == 6: return queen_moves(idx)
    if val == 9 or val == 1: return king_moves(idx)
    return []

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



def is_stalemate(index):
    piece_value = board[index]
    if piece_value == 1:
        if is_square_safe(index) == True and len(king_moves(index)) == 0:
            for i in range(64):
                piece = board[i]
                if 0<piece<8:
                    possible_moves = get_moves_for_piece(i,piece)
                    if len(possible_moves)==0:
                        continue
                    return True
    elif piece_value == 9:
        if is_square_safe(index) == True and len(king_moves(index)) == 0:
            for i in range(64):
                piece = board[i]
                if 8<piece<16:
                    possible_moves = get_moves_for_piece(i,piece)
                    if len(possible_moves)==0:
                        return True
    return False




        
        

