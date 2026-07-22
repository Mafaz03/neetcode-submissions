class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r, deleted: bool):

            if l >= r:
                return True

            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    return isPalindrome(l+1, r, True) or isPalindrome(l, r-1, True)
            
            else:
                return isPalindrome(l + 1, r - 1, deleted)

        return isPalindrome(0, len(s)-1, False)


