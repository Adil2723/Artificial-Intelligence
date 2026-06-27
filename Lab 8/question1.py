import math
import os

ROWS, COLS = 6, 7
EMPTY      = " "
PLAYER     = "X"
AI         = "O"
WINDOW     = 4          
AI_DEPTH   = 5          

def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

def drop_piece(board, col, piece):
    """Place piece in the lowest empty row of col. Returns row index, or -1."""
    for r in reversed(range(ROWS)):
        if board[r][col] == EMPTY:
            board[r][col] = piece
            return r
    return -1

def valid_moves(board):
    """Columns that still have room."""
    return [c for c in range(COLS) if board[0][c] == EMPTY]

def is_full(board):
    return len(valid_moves(board)) == 0

def copy_board(board):
    return [row[:] for row in board]

def check_win(board, piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(WINDOW)):
                return True
    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(WINDOW)):
                return True
    # Diagonal ↘
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(WINDOW)):
                return True
    # Diagonal ↗
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(WINDOW)):
                return True
    return False

def is_terminal(board):
    return check_win(board, PLAYER) or check_win(board, AI) or is_full(board)

def score_window(window, piece):

    opp = PLAYER if piece == AI else AI

    own  = window.count(piece)
    emp  = window.count(EMPTY)
    opp_ = window.count(opp)

    if own == 4:              return 100
    if own == 3 and emp == 1: return  10
    if own == 2 and emp == 2: return   4
    if opp_ == 3 and emp == 1: return -20   # block urgent threat
    return 0

def evaluate(board, piece):

    score = 0

    # Centre column preference
    centre_col = [board[r][COLS // 2] for r in range(ROWS)]
    score += centre_col.count(piece) * 6

    # Horizontal windows
    for r in range(ROWS):
        for c in range(COLS - 3):
            w = [board[r][c + i] for i in range(WINDOW)]
            score += score_window(w, piece)

    # Vertical windows
    for c in range(COLS):
        for r in range(ROWS - 3):
            w = [board[r + i][c] for i in range(WINDOW)]
            score += score_window(w, piece)

    # Diagonal ↘
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            w = [board[r + i][c + i] for i in range(WINDOW)]
            score += score_window(w, piece)

    # Diagonal ↗
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            w = [board[r - i][c + i] for i in range(WINDOW)]
            score += score_window(w, piece)

    return score

_stats = {"nodes": 0, "pruned": 0}

def minimax(board, depth, alpha, beta, maximising):
    """
    Adversarial search.
      maximising=True  → AI's turn  (maximise score)
      maximising=False → Player's turn (minimise score)
    """
    _stats["nodes"] += 1

    terminal = is_terminal(board)

    # Terminal / leaf evaluation
    if terminal:
        if check_win(board, AI):     return  math.inf   # AI wins
        if check_win(board, PLAYER): return -math.inf   # Player wins
        return 0                                        # Draw

    if depth == 0:
        return evaluate(board, AI)

    moves = valid_moves(board)

    if maximising:
        value = -math.inf
        for col in moves:
            nb = copy_board(board)
            drop_piece(nb, col, AI)
            value = max(value, minimax(nb, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:           # β-cutoff
                _stats["pruned"] += 1
                break
        return value
    else:
        value = math.inf
        for col in moves:
            nb = copy_board(board)
            drop_piece(nb, col, PLAYER)
            value = min(value, minimax(nb, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:           # α-cutoff
                _stats["pruned"] += 1
                break
        return value

def best_move(board, depth=AI_DEPTH):
    """Return the column index of the AI's optimal move."""
    _stats["nodes"]  = 0
    _stats["pruned"] = 0

    best_score = -math.inf
    best_col   = valid_moves(board)[0]      # safe fallback

    for col in valid_moves(board):
        nb = copy_board(board)
        drop_piece(nb, col, AI)
        score = minimax(nb, depth - 1, -math.inf, math.inf, False)
        if score > best_score:
            best_score = score
            best_col   = col

    return best_col, best_score

def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("  " + "   ".join(str(c) for c in range(COLS)))
    print("  " + "---" * COLS + "-")
    for row in board:
        cells = []
        for cell in row:
            if cell == PLAYER:
                cells.append("\033[93mX\033[0m")   # yellow X
            elif cell == AI:
                cells.append("\033[91mO\033[0m")   # red O
            else:
                cells.append("·")
        print("| " + " | ".join(cells) + " |")
        print("  " + "---" * COLS + "-")
    print()


def play():
    print("\n" + "=" * 44)
    print("   Connect Four  |  You = \033[93mX\033[0m   AI = \033[91mO\033[0m")
    print(f"   AI search depth: {AI_DEPTH}")
    print("=" * 44)

    board  = create_board()
    turn   = PLAYER      # player always goes first

    while True:
        print_board(board)

        if turn == PLAYER:
            moves = valid_moves(board)
            while True:
                try:
                    col = int(input(f"  Your move — choose column {moves}: "))
                    if col not in moves:
                        print("  Column full or out of range, try again.")
                        continue
                    break
                except (ValueError, EOFError):
                    print("  Enter a column number (0-6).")

            drop_piece(board, col, PLAYER)

            if check_win(board, PLAYER):
                print_board(board)
                print("  \033[93mYou win! Congratulations!\033[0m")
                break
            if is_full(board):
                print_board(board)
                print("  It's a draw!")
                break
            turn = AI

        else:
            print("  AI is thinking …")
            col, score = best_move(board)
            drop_piece(board, col, AI)
            print(f"  AI played column {col}  "
                  f"[nodes={_stats['nodes']:,}  pruned={_stats['pruned']:,}  score={score}]")

            if check_win(board, AI):
                print_board(board)
                print("  \033[91mAI wins!\033[0m")
                break
            if is_full(board):
                print_board(board)
                print("  It's a draw!")
                break
            turn = PLAYER

    again = input("\n  Play again? (y/n): ").strip().lower()
    if again == "y":
        play()
    else:
        print("  Thanks for playing!\n")

if __name__ == "__main__":
    play()
