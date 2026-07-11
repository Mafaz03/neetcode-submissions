class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # pre_sort_hash = {i: idx for idx, i in enumerate(queries)}

        # queries = sorted(queries)

        # post_sort_hash = {i: idx for idx, i in enumerate(queries)}

        # sort_hash = {}
        # for k,v in pre_sort_hash.items():
        #     sort_hash[v] = post_sort_hash[k]

        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))

        def sort_len(x):
            return x[0]

        intervals = sorted(intervals, key = sort_len)

        heap = []


        res = [-1] * len(queries)

        # q = queries[0]

        i = 0
        for q, idx in sorted_queries:
            

            
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                # print(heap)
                i += 1

            while heap and heap[0][1] < q:
                # print("no")
                heapq.heappop(heap)
                
            res[idx] = heap[0][0] if heap else -1

        # new_res = [0] * len(res)

        # for pre, post in sort_hash.items():
        #     new_res[pre] = res[post]

        return res