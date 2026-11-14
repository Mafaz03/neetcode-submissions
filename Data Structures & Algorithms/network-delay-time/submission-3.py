class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dij_hash = {node: float("inf") for node in range(1, n + 1)}
        dij_hash[k] = 0
        
        graph = defaultdict(list)
        for a, b, t in times:
            graph[a].append((b, t))
        
        heap = [] # weight, node

        heapq.heappush(heap, (k, 0))

        while heap:
            curr_node, curr_cost = heapq.heappop(heap)

            if curr_cost > dij_hash[curr_node]:
                continue # already found cheaper path to current node
            
            for nei, nei_cost in graph[curr_node]:
                
                distance_to_nei = curr_cost + nei_cost

                if distance_to_nei < dij_hash[nei]:
                    dij_hash[nei] = distance_to_nei
                    heapq.heappush(heap, (nei, distance_to_nei))
        # print(dij_hash)

        res = max(dij_hash.values())
        return res if res != float("inf") else -1
