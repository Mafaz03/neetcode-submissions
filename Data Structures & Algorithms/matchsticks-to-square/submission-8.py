class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        matchsticks.sort()
        target = sum(matchsticks)/4

        if not target.is_integer(): return False
        else: target = int(target)

        dp = {}

        def backtrack(sides, idx):
            if (tuple(sides), idx) in dp:
                return dp[(tuple(sides), idx)]

            if all(side == target for side in sides):
                return True
                
            if all(side >= target for side in sides):
                return False

            if idx == len(matchsticks):
                return False

            for s in range(4):
                sides[s] += matchsticks[idx]
                idx += 1

                if backtrack(sides, idx): 
                    return True

                else:
                    dp[(tuple(sides), idx)] = False

                idx -= 1
                sides[s] -= matchsticks[idx]

        return True if backtrack([0,0,0,0], 0) else False