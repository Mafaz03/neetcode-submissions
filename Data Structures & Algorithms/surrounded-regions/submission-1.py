class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        O_connected = {}
        visited = set()

        def bfs(O_grp, r, c):
            dq = deque([])
            dq.append((r,c))
            O_connected[O_grp] = {(r,c)}

            while dq:
                r, c = dq.popleft()
                for r_off, c_off in [(0,1), (1,0), (-1,0), (0,-1)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols) and ((row,col) not in visited) and (board[row][col] == "O"):
                        visited.add((row,col))
                        dq.append((row,col))
                        O_connected[O_grp].add((row,col))
                    

            return O_grp + 1


        O_grp = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    O_grp = bfs(O_grp, i,j)

        to_flip = set()

        for i in range(len(O_connected)):
            surrounded = False
            for r,c in O_connected[i]:
                for r_off, c_off in [(0,1), (1,0), (-1,0), (0,-1)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols):
                        surrounded = True
                    else:
                        surrounded = False
                        break
                if not surrounded:
                    break

            if surrounded:
                for r,c in O_connected[i]:
                    to_flip.add((r,c))

        # flipping
        for r,c in to_flip:
            board[r][c] = "X"