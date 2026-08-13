class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x: x[0])

        meetings_min_heap = []

        rooms_min_heap = list(range(n))
        heapq.heapify(rooms_min_heap)

        room_counter = {i: 0 for i in range(n)}

        for start, end in meetings:
            
            # free meeting rooms
            while ((meetings_min_heap) and (meetings_min_heap[0][0] <= start)):
                _, new_room = heapq.heappop(meetings_min_heap)
                heapq.heappush(rooms_min_heap, new_room)
            
            # if room is avaialble use it
            if (rooms_min_heap):
                new_room = heapq.heappop(rooms_min_heap)
                heapq.heappush(meetings_min_heap, (end, new_room))
            
            # delay meeting
            else:
                new_end, new_room = heapq.heappop(meetings_min_heap)
                duration = end - start
                heapq.heappush(meetings_min_heap, (new_end + duration, new_room))
            
            room_counter[new_room] += 1


        print(room_counter)

        m = max(room_counter.values())
        for k, v in room_counter.items():
            if v == m:
                return k