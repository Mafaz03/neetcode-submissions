class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        if len(t) == len(s): 
            print("here")
            return s if Counter(s) == Counter(t) else ""

        t_hash = Counter(t)
        window_hash = {k: 0 for k, _ in t_hash.items()}

        need = len(t_hash)
        have = 0

        L, R = 0, 0

        min_length = float("inf")
        min_idx = []

        while R < len(s):
            # check condition
            if s[R] in window_hash:
                window_hash[s[R]] += 1

                if window_hash[s[R]] == t_hash[s[R]]:
                    have += 1
            
            while have == need:
                if R-L+1 < min_length:
                    min_length = R-L+1
                    min_idx = [L,R]    

                if s[L] in window_hash:
                    if window_hash[s[L]] == t_hash[s[L]]:
                        have -= 1
                    
                    window_hash[s[L]] -= 1
        
                L += 1
            R += 1

        return s[min_idx[0]: min_idx[1] + 1] if min_idx else ""