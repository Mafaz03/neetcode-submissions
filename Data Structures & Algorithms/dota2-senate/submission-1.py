class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque([])
        d = deque([])

        n = len(senate)

        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            r_ele = r.popleft()
            d_ele = d.popleft()

            if r_ele < d_ele:
                r.append(r_ele + n)
            else:
                d.append(d_ele + n)
            
        return "Radiant" if r else "Dire"