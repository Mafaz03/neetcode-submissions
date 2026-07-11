class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_sub = 0
        max_str = ""

        for i in range(len(s)):
            r = l = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if r-l+1 > max_sub:
                    max_sub = r-l
                    max_str = s[l:r+1]

                l -= 1
                r += 1
            
            l = i
            r = i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if r-l+1 > max_sub:
                    max_sub = r-l
                    max_str = s[l:r+1]

                l -= 1
                r += 1
        return max_str