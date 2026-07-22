class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False
        freq = Counter(nums[:k+1])

        idx1 = 0
        idx2 = k

        while idx2 < len(nums) - 1:
            if len(freq) <= k: return True

            freq[nums[idx1]] -= 1

            if freq[nums[idx1]] == 0:
                del freq[nums[idx1]]

            idx1 += 1
            idx2 += 1

            freq[nums[idx2]] += 1
        if len(freq) <= k: return True
        return False