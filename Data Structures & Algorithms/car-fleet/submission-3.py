class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if len(position) == 1: return 1
        sorted_arr = sorted(zip(position, speed), reverse=True)
        
        pos = []
        spe = []

        for i in sorted_arr:
            pos.append(i[0])
            spe.append(i[1])

        unit_times = []
        for idx in range(len(pos)):
            t = (target - pos[idx])/spe[idx]
            unit_times.append(t)
        
        print(unit_times)

        stack = []
        stack.append(unit_times[0])

        
        for idx in range(0, len(pos)):
            if stack and unit_times[idx] > stack[-1]:
                stack.append(unit_times[idx])

        print(stack)
        return len(stack)

        # fleet = 1

        # for idx in range(1, len(pos)):
        #     if unit_times[idx-1] < unit_times[idx]:
        #         fleet += 1

        # return fleet




