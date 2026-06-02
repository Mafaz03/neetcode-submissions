class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        L = 0

        maximum = 0
        count = {}

        for R in range(n):
            count[s[R]] = 1 + count.get(s[R], 0)

            most_freq = max(count.values())

            valid_cond = ((R - L + 1) - most_freq) <= k

            if not valid_cond:
                count[s[L]] -= 1
                L += 1

            maximum = max(maximum, R - L + 1)
        return maximum