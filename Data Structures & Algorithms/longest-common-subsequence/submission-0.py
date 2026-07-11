class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row_prev = [0] * (len(text1)+1)

        for i in reversed(range(len(text2))):
            row_new = [0] * (len(text1) + 1)
            
            for j in reversed(range(len(text1))):
                
                if text2[i] == text1[j]:
                    print("wow")
                    row_new[j] =  1 + row_prev[j+1]
                else:
                    row_new[j] = max(row_prev[j], row_new[j+1])
            
            # print(row_prev)
            row_prev = row_new
        return row_prev[0]