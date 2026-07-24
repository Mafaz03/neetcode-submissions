class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def howMany(s):
            currSum = 0
            partitions = 1
            for n in nums:
                currSum += n

                if currSum > s:
                    currSum = n
                    partitions += 1
                if partitions > k: return False
            return False if  partitions > k else True

        L = max(nums)
        R = sum(nums)

        res = float("inf")

        while L <= R:
            mid = (L+R)//2

            if howMany(mid):
                res = min(res, mid)
                R = mid - 1
            else:
                L = mid + 1

        return res