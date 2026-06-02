class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        L = 0

        maximum = 0
        count = {}

        maxf = 0

        for R in range(n):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(maxf, count[s[R]])

            # most_freq = max(count.values())

            valid_cond = ((R - L + 1) - maxf) <= k

            if not valid_cond:
                count[s[L]] -= 1
                L += 1

            maximum = max(maximum, R - L + 1)
        return maximum