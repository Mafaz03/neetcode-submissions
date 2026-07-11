class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        visited = set()
        dir_idx = 0

        idx = [0,0]

        while len(visited) != rows*cols:
            
            if (idx[0], idx[1]) not in visited:
                # print(matrix[idx[0]][idx[1]])
                res.append(matrix[idx[0]][idx[1]])
                visited.add((idx[0], idx[1]))

            if dir_idx == 0:
                if (idx[1]+1 == cols) or ((idx[0], idx[1]+1) in visited):
                    dir_idx += 1
                else:
                    idx[1] += 1
            
            elif dir_idx == 1:
                if (idx[0]+1 == rows) or ((idx[0]+1, idx[1]) in visited):
                    dir_idx += 1
                else:
                    idx[0] += 1
            
            elif dir_idx == 2:
                if (idx[1]-1 == -1) or ((idx[0], idx[1]-1) in visited):
                    dir_idx += 1
                else:
                    idx[1] -= 1
            
            elif (dir_idx) == 3:
                if (idx[0]-1 == -1) or ((idx[0]-1, idx[1]) in visited):
                    dir_idx += 1
                else:
                    idx[0] -= 1
            

            dir_idx = dir_idx % 4
        return res