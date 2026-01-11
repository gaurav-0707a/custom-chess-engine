board = [0]*64
def notations(row,column):
    position = 8*(7-row) + column
    return position
piece_map = {
    'k': 1, 'q': 6, 'r': 5, 'b': 4, 'n': 3, 'p': 2,  # Black
    'K': 9, 'Q': 14, 'R': 13, 'B': 12, 'N': 11, 'P': 10 # White 
}
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
print(board)
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
def knight_moves(index):
    knight_possibility = [index-17,index-15,index-10,index-6,index+6,index+10,index+15,index+17]
    knight = 0
    knights = 0
    while knight < (len(knight_possibility)):
        if knight_possibility[knight] > 63 or knight_possibility[knight] < 0:
            knight_possibility.remove(knight_possibility[knight])
        else:
            knight+=1
    print(knight_possibility)
    while knights <(len(knight_possibility)):
        if board[knight_possibility[knights]] > 0:
            knight_possibility.remove(knight_possibility[knights])
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
# Code for capturing pieces now!


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
            kings_possibility.remove(kings_possibility[king])
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
# Code for capturing pieces now

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
    return rook_possibility
# Code for capture now!


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
# code for captures now

def queen_move(index):
    


    


    
    

  