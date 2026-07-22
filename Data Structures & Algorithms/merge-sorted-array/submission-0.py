class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = len(nums1)-1

        k = n - 1

        while k >= 0:
            if i >= 0 and nums1[i] >= nums2[k]:
                nums1[j] = nums1[i]
                i -= 1
            else:
                nums1[j] = nums2[k]
                k -= 1
            j -= 1

        nums1
        