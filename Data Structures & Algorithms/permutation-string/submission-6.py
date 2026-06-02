class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = Counter(s1)

        n = len(s1)
        m = len(s2)

        for idx in range(0, m-n+1):
            c_temp = Counter(s2[idx: idx + n])
            if c1 == c_temp: return True
        
        return False