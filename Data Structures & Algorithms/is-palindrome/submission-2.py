class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx_1 = 0
        idx_2 = len(s)-1

        while idx_1 < idx_2:
            if not s[idx_1].isalnum(): 
                idx_1 += 1
                continue
            if not s[idx_2].isalnum(): 
                idx_2 -= 1
                continue
            # print(s[idx_1].lower(), s[idx_2].lower())
            if s[idx_1].lower() != s[idx_2].lower(): return False
            idx_1 += 1 
            idx_2 -= 1 
        
        return True