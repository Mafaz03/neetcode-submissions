class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def join(left, right):
            res = []

            idx_l = 0
            idx_r = 0
            
            while (idx_l != len(left)) and ((idx_r) != len(right)):
                if (left[idx_l] <= right[idx_r]):
                    res.append(left[idx_l])
                    idx_l += 1
                else:
                    res.append(right[idx_r])
                    idx_r += 1
            
            res.extend(left[idx_l:])
            res.extend(right[idx_r:])

            return res

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            
            return join(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
            

        return mergeSort(nums)