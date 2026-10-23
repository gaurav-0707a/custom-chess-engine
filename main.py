"""Entry point: load a position, pick a depth, play White against the engine (Black)."""

from engine.board import board, load_fen, print_board
from engine.moves import get_moves_for_piece
from engine.rules import is_checkmate, is_legal, check_and_promote
from engine.search import get_best_move


def main():
    print("paste the FEN string of the position:")
    fen_string = str(input())
    load_fen(fen_string)

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


if __name__ == "__main__":
    main()
