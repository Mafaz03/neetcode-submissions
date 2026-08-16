class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        d = []

        n = len(arr)
        if n == 1: return 1

        for i in range(1, n):
            # if d == 0: continue  # making sure 0 is considered positive
            d.append(arr[i-1] - arr[i])

        # If every difference is 0
        if all(x == 0 for x in d):
            return 1
        
        n -= 1
        # print(d)

        max_tur = 2

        if d[0] == 0:
            t = 1
        else:
            t = 2 

        for i in range(n-1):
            # print("in question: ", d[i], d[i+1])
            
            if (d[i+1] == 0):
                t = 1
            
            elif (d[i] == 0):
                t = 2

            elif (d[i] <= 0 and d[i+1] > 0) or (d[i] >= 0 and d[i+1] < 0):
                t += 1
            else:
                t = 2

            # print("t: ", t)
            max_tur = max(max_tur, t)
            # print("max: ", max_tur)
            # print("\n")
        
        # return max(2, max_tur) # it can only occur in pairs (2 is minimim)
        return max_tur
         



