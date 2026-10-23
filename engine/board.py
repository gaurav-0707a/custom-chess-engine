board = [0]*64
piece_map = {
    'k': 1, 'q': 6, 'r': 5, 'b': 4, 'n': 3, 'p': 2,  # Black
    'K': 9, 'Q': 14, 'R': 13, 'B': 12, 'N': 11, 'P': 10 # White 
}

piece_presentation = {
    1: 'k', 6:'q', 5:'r', 4:'b', 3:'n', 2:'p',  # Black
    9:'K', 14:'Q', 13:'R', 12:'B', 11:'N', 10:'P' # White 
}


def load_fen(fen_string):
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
