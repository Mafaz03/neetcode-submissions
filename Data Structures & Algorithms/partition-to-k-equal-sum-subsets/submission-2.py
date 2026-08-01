class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)/k

        if not target.is_integer():
            return False
        
        target = int(target)

        seen = set() # {sums: t or f}

        def backtrack(sums: list, idx: int):

            if all(s == target for s in sums):
                return True

            if idx == len(nums):
                return False

            state = (tuple(sorted(sums)), idx)
            if state in seen:
                return False

            for s_idx in range(k):
                if sums[s_idx] + nums[idx] <= target:
                    sums[s_idx] += nums[idx]
                    idx += 1
                    if backtrack(sums, idx):
                        return True

                    idx -= 1
                    sums[s_idx] -= nums[idx]
            
            seen.add(state)

            return False

        return backtrack([0]*k, 0)