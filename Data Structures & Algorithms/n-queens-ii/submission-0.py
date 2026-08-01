class Solution:
    def totalNQueens(self, n: int) -> int:
        col_queen_in = set()
        pos_diag     = set()
        neg_diag     = set()

        res =[0]

        def backtrack(row):
            if row == n:
                res[0] += 1
                return 

            for col in range(n):
                if (col not in col_queen_in) and ((row + col) not in pos_diag) and ((row-col) not in neg_diag):

                    col_queen_in.add(col)
                    pos_diag.add(row+col)
                    neg_diag.add(row-col)

                    backtrack(row + 1)

                    col_queen_in.remove(col)
                    pos_diag.remove(row+col)
                    neg_diag.remove(row-col)

        backtrack(0) 

        return res[0]