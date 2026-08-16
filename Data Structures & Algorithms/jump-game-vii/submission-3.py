class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # n = len(s)
        # dp = [False for _ in range(n)]

        # dp[0] = True

        # # find the next True idx
        # for i in range(n):
        #     if (s[i] == "0") and dp[i] == True:
        #         for j in range(i + minJump, min(i + maxJump + 1, n)):
        #             if s[j] == '0':
        #                 dp[j] = True

        # print(dp)
        # return dp[-1]

        n = len(s)
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest)
            end   = min(i + maxJump + 1, n)
            
            for j in range(start, end):
                if s[j] == "0":
                    q.append(j)
                    if j == n-1:
                        return True

            farthest = i + maxJump
        return False
                
                

