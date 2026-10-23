# custom-chess-engine

A chess engine I wrote in plain Python, no libraries. You play White in the terminal and the engine plays Black.

I wanted to understand how engines actually work, so everything is hand-written: reading a FEN, generating moves for each piece, checking whether a move leaves your king in danger, and a minimax search on top.

## Running it

You need Python 3. From the project folder:

```
python main.py
```

It asks for two things:

1. **A FEN string.** Paste only the board part, not the full thing. For the normal starting position:
   ```
   rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
   ```
   (If you paste the `w KQkq - 0 1` bit at the end it crashes, I haven't fixed that yet.)
2. **Search depth.** 1 is instant, 2 takes a second or two, 3 is slow (30 to 60 seconds) because there's no pruning.

## movements

The board is numbered 0 to 63, starting at the top-left corner and going row by row:

```
 0  1  2  3  4  5  6  7     <- Black's side
 8  9 10 11 12 13 14 15
 ...
48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63     <- White's side
```

Type the number of the piece you want to move. It prints the squares that piece can go to, then you type the target number. For example, `52` then `36` plays e2 to e4.

## Working

- The board is a flat list of 64 numbers. Black pieces are 1 to 6 and White pieces are 9 to 14, so checking a piece's colour is just a range check.
- Every piece has its own move function. A move is only allowed if it doesn't leave your own king attacked.
- The evaluation uses the PeSTO piece values and piece-square tables. It uses the endgame tables once both queens are gone.
- The search is plain recursive minimax.

## Project layout

```
main.py              game loop
engine/
    board.py         board list, FEN loading, printing
    tables.py        piece values and piece-square tables
    moves.py         move generation
    rules.py         king safety, legal moves, checkmate, promotion
    evaluation.py    scoring a position
    search.py        minimax
```

## to be updated

- No castling, no en passant. Pawns always promote to a queen.
- No stalemate, repetition or 50-move rule.
- No alpha-beta pruning, so anything past depth 3 is too slow.
- Checkmate detection is unreliable. It only looks at whether the king has any physical moves, not whether those squares are attacked, so some mates (fool's mate, for one) get missed.
- White's h-pawn can't double push from the start, so White has 19 opening moves instead of 20.

Alpha-beta pruning and fixing the checkmate check are next.

The evaluation tables come from the PeSTO function on the Chess Programming Wiki. I followed Sebastian Lague's videos to understand minimax and alpha-beta.
