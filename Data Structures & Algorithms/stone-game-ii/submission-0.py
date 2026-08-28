class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def dfs(alice: bool, index: int, M):

            # Check if we already solved this state
            if (alice, index, M) in memo:
                return memo[(alice, index, M)]

            if index >= len(piles):
                return 0

            res = 0 if alice else float("inf")
            total = 0

            for i in range(1, (2 * M) + 1):

                if index + i > len(piles):
                    break

                total += piles[index + i - 1]

                if alice:  # Alice tries to maximize Alice's score
                    res = max(
                        res,
                        total + dfs(False, index + i, max(M, i))
                    )

                else:      # Bob tries to minimize Alice's score
                    res = min(
                        res,
                        dfs(True, index + i, max(M, i))
                    )

            # Store the answer for this state
            memo[(alice, index, M)] = res

            return res

        return dfs(True, 0, 1)