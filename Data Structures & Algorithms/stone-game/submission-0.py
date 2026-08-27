class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        left  = 0
        right = n-1

        alice = 0
        bob   = 0

        chance = 0

        while left < right:

            if piles[left] > piles[right]:
                points = piles[left]
                left += 1
            else:
                points = piles[right]
                right -= 1
            
            if chance % 2 == 0:
                alice += points
            else:
                bob += points
            
            return alice > bob