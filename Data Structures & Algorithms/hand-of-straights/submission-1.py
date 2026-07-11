class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        counter_hash = Counter(hand)

        if len(hand) % groupSize != 0: return False

        for _ in range(len(hand)//groupSize):
            ele_in_qestion = min(counter_hash.keys())
            for i in range(groupSize):
                if (ele_in_qestion + i) in counter_hash:
                    counter_hash[ele_in_qestion + i] -= 1
                    if counter_hash[ele_in_qestion + i] == 0:
                        del counter_hash[ele_in_qestion + i]

        return True if len(counter_hash) == 0 else False