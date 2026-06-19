def placeQueen(board, x, y):

    not_allowed = []
    # row
    for j in range(len(board[0])):
        if j != y:
            not_allowed.append([x,j])

    # column
    for i in range(len(board)):
        if i != x:
            not_allowed.append([i,y])

    # down-right
    i, j = x, y
    while i + 1 < len(board) and j + 1 < len(board[0]):
        i += 1
        j += 1
        not_allowed.append([i,j])

    # down-left
    i, j = x, y
    while i + 1 < len(board) and j - 1 >= 0:
        i += 1
        j -= 1
        not_allowed.append([i,j])

    # up-right
    i, j = x, y
    while i - 1 >= 0 and j + 1 < len(board[0]):
        i -= 1
        j += 1
        not_allowed.append([i,j])

    # up-left
    i, j = x, y
    while i - 1 >= 0 and j - 1 >= 0:
        i -= 1
        j -= 1
        not_allowed.append([i,j])

    return not_allowed



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(board, not_possible, row_idx):

            if row_idx == len(board):
                res.append(["".join(row) for row in board])
                return
            
            for col in range(len(board[0])):
                if [row_idx, col] not in not_possible and row_idx < len(board) and col < len(board):
                    board[row_idx][col] = "Q"
                    backtrack(board, not_possible + placeQueen(board, row_idx, col), row_idx+1)
                    board[row_idx][col] = "."
        
        board = []
        for i in range(n):
            t = []
            for j in range(n):
                t.append(".")
            board.append(t)

        backtrack(board, [], 0)
        return res
        