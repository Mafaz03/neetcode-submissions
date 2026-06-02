class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        s1 = sorted([ord(i) for i in s1])
        for idx in range(0, m-n+1):
            s2_temp = sorted([ord(i) for i in s2[idx: idx + n]])
            if s1 == s2_temp: return True
        return False
        
        # c1 = Counter(s1)

        # for idx in range(0, m-n+1):
        #     c_temp = Counter(s2[idx: idx + n])
        #     if c1 == c_temp: return True
        
        # return False