class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2

        cache = {}

        def subset(index, total):
            if total > target:
                return 0
            
            if index == len(stones):
                return total

            if (index, total) in cache:
                return cache[(index, total)]

            take = subset(index + 1, total + stones[index]) 
            skip = subset(index + 1, total) 

            res = max(take, skip)

            cache[(index, total)] = res

            return res

            
        best = subset(0, 0)
        return sum(stones) - (2 * best)