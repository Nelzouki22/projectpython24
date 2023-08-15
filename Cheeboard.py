def print_chessboard(board):
    for row in board:
        print(" ".join(row))

def create_chessboard():
    board = []
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append("-")
        board.append(row)
    return board

chessboard = create_chessboard()
print_chessboard(chessboard)
