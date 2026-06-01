class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # searching row
        L, R = 0, len(matrix)
        row_idx = None
        col_idx = None

        if not target > matrix[-1][-1] and not target < matrix[0][0]:
            while L <= R:
                mid = (L + R)//2
                # print(L, mid, R)

                if (matrix[mid][0] <= target <= matrix[mid][-1]):
                    row_idx = mid
                    # print("found: ,", row_idx)
                if matrix[mid][-1] < target:
                    L = mid + 1
                else:
                    R = mid - 1

        if row_idx is not None:
            L, R = 0, len(matrix[0])
            

            while L <= R:
                mid = (L+R)//2
                if matrix[row_idx][mid] == target:
                    col_idx = mid
                
                if matrix[row_idx][mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1

        return True if col_idx is not None else False