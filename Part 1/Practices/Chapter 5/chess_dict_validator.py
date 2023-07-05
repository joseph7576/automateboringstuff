from collections import Counter

# '1a' to '8h' -> moves
# 'w' for white, 'b' for black -> first char in string
# one black king, one white king, each player have 16 pieces, 8 pawns
# King, Queen, Rook, Bishop, kNight

# sample chess board
# move: piece
chess_board = {'1h': 'bking', 
               '6c': 'wqueen', 
               '2g': 'bbishop', 
               '5h': 'bqueen', 
               '3e': 'wking'}

#                  8        2         2        2       1        1   -> number of pieces
VALID_PIECES = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
VALID_NUMBER_LOC = [str(i) for i in range(1,9)]
VALID_CHAR_LOC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
VALID_COLORS = ['w', 'b']

# make a list of all valid moves
ALL_VALID_MOVE = []
for number in VALID_NUMBER_LOC:
    for char in VALID_CHAR_LOC:
        ALL_VALID_MOVE.append(number + char) # '1a'

# make a list of all valid pieces
ALL_VALID_PIECE = []
for color in VALID_COLORS:
    for pieces in VALID_PIECES:
        ALL_VALID_PIECE.append(color + pieces) # 'wking'

# make a dict of all valid piece count
VALID_COUNTER = {}
for valid_piece in ALL_VALID_PIECE:
    if 'pawn' in valid_piece:
        VALID_COUNTER[valid_piece] = 8
    elif 'knight' in valid_piece or 'bishop' in valid_piece or 'rook' in valid_piece:
        VALID_COUNTER[valid_piece] = 2
    elif 'queen' in valid_piece or 'king' in valid_piece:
        VALID_COUNTER[valid_piece] = 1


def isValidChessBoard(chess_board:dict):
    # unpack dict into separate lists
    move_list = list(chess_board.keys())
    piece_list = list(chess_board.values())
    
    # check movesa
    for move in move_list:
        if move not in ALL_VALID_MOVE:
            print(f'{move} is not a valid move!')
            return False
            
    # check piece count
    piece_counter = Counter(piece_list)
    
    for piece, count in piece_counter.items():
        if count > VALID_COUNTER[piece]:
            print(f'There is {count} {piece} in chess board, It should be less than {VALID_COUNTER[piece]}!')
            return False
    
    # check total piece count
    piece_sum = sum(piece_counter.values())
    valid_sum = sum(VALID_COUNTER.values())
    
    if piece_sum > valid_sum:
        print(f'There are total of {piece_sum} in chess board, It should be {valid_sum}!')
        return False
    
    # check pieces
    for piece in piece_list:
        # check piece stirng
        piece_color = piece[0] # slice the first char -> color
        chess_piece = piece[1:] # extract piece from color+piece

        # check piece color
        if piece_color not in ['w', 'b']:
            print(f'{piece} is no a valid piece color!')
            return False
            
        # check piece
        if chess_piece not in VALID_PIECES:
            print(f'{piece} is not a valid piece!')
            return False
            
    return True
    
result = isValidChessBoard(chess_board) # -> valid chess board
print(result)
        