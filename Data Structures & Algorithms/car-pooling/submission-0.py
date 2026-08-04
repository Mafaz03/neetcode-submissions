class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pick_drop = {}

        for passengers, to, go in trips:

            if (to not in pick_drop):
                pick_drop[to] = [0, 0]

            if (go not in pick_drop):
                pick_drop[go] = [0, 0]

            pick_drop[to][0] += passengers
            pick_drop[go][1] += (-passengers)

        print(pick_drop)

        idxs = sorted(list(pick_drop.keys()))

        count = 0

        for i in idxs:
            count += (pick_drop[i][0] + pick_drop[i][1])
            print(count)
            if count > capacity:
                return False
        return True




