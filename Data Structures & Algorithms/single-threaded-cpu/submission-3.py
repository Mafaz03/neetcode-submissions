class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [i + [idx] for idx, i in enumerate(tasks)]

        tasks = sorted(tasks, key = lambda x: x[0])
        
        def flip(x): return [x[1], x[2], x[0]]

        heap = []

        tasks_idx = 0
        time = tasks[0][0]

        while (tasks_idx < len(tasks)) and (tasks[tasks_idx][0] <= time):
            heapq.heappush(heap, flip(tasks[tasks_idx]))
            tasks_idx += 1

        idx = []


        while heap:
            p_time, index, enq_time = heapq.heappop(heap)
            idx.append(index)
            
            time += p_time

            while tasks_idx < len(tasks) and tasks[tasks_idx][0] <= time:
                heapq.heappush(heap, flip(tasks[tasks_idx]))
                tasks_idx += 1
            
            if (not heap) and (tasks_idx < len(tasks)):
                time = tasks[tasks_idx][0]
                heapq.heappush(heap, flip(tasks[tasks_idx]))
                tasks_idx += 1

        return idx