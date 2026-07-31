class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        seen = set()
        matchsticks.sort(reverse=True)
        target = sum(matchsticks)/4

        if not target.is_integer(): return False
        else: target = int(target)

        def backtrack(sides, idx):
    
            if all(side == target for side in sides):
                return True

            if idx == len(matchsticks):
                return False

            if tuple(sides) not in seen:
                for s in range(4):
                    if sides[s] + matchsticks[idx] <= target:
                        sides[s] += matchsticks[idx]
                        idx += 1

                        if backtrack(sides, idx): 
                            return True

                        idx -= 1
                        sides[s] -= matchsticks[idx]
            seen.add(tuple(sides))
            
            return False

        return backtrack([0,0,0,0], 0)