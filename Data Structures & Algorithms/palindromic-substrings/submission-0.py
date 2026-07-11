class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = []

        for i in range(len(s)):
            r = l = i

            while (l >= 0 and r < len(s)) and s[r] == s[l]:
                palindromes.append(s[l:r+1])

                r += 1
                l -= 1
            
            r = i+1
            l = i

            while (l >= 0 and r < len(s)) and s[r] == s[l]:
                palindromes.append(s[l:r+1])

                r += 1
                l -= 1

        return len(palindromes)