class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        atlantic_dq = deque([])
        pacific_dq  = deque([])

        atlantic_visited = set()
        pacific_visited  = set()

        for i in range(rows-1):
            atlantic_dq.append((i,cols-1))
        for i in range(cols):
            pacific_dq.append((0,i))

        for i in range(cols):
            atlantic_dq.append((rows-1,i))
        for i in range(1,rows):
            pacific_dq.append((i,0))

        while atlantic_dq:
            for _ in range(len(atlantic_dq)):
                r, c = atlantic_dq.popleft()
                atlantic_visited.add((r,c))
                

                for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols) and ((row,col) not in atlantic_visited) and (heights[row][col] >= heights[r][c]):
                        atlantic_dq.append((row,col))
                        

        while pacific_dq:
            for _ in range(len(pacific_dq)):
                r, c = pacific_dq.popleft()
                pacific_visited.add((r,c))
                

                for r_off, c_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                    row = r + r_off
                    col = c + c_off

                    if (0 <= row < rows) and (0 <= col < cols) and ((row,col) not in pacific_visited) and (heights[row][col] >= heights[r][c]):
                        pacific_dq.append((row,col))

        return list(atlantic_visited.intersection(pacific_visited))