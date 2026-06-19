class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        if rows == 1 and cols == 1:
            if board[0][0] == word: return True 
            else: return False


        def backtrack(i, j, w_idx: str):
            if w_idx == len(word): 
                return True
            
            w = word[w_idx]

            if board[i][j] != w:
                return False

            ch = board[i][j]
            board[i][j] = "67"

            
            for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                if (0 <= i + i_off < rows) and (0 <= j + j_off < cols):
                    if backtrack(i + i_off, j + j_off, w_idx + 1):
                        return True

            board[i][j] = ch
            return False
            


        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False