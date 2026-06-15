class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        def dfs(i, subset, total):
    
            if total == target:
                # print(subset.copy())
                if subset not in res:
                    res.append(subset.copy())
                return
            
            if i >= len(candidates):
                return 
            
            if total > target:
                return 

            if total + candidates[i] > target:
                return
            
            subset.append(candidates[i])
            total += candidates[i]

            dfs(i + 1, subset, total)

            subset.pop()
            
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1


            dfs(next_i, subset, total-candidates[i])

        dfs(0, [], 0)
        return res