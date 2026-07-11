class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = {}

        for idx in range(numCourses):
            hashmap[idx] = []

        for i in prerequisites:
            hashmap[i[0]].append(i[1])

        # print(hashmap)
        path = set()

        def dfs(node_idx):

            if node_idx in path:
                return False  # cycle found
            
            if len(hashmap[node_idx]) == 0:
                return True
            
            path.add(node_idx)
            
            # print(hashmap[node_idx])
            for nei in hashmap[node_idx]:
                if not dfs(nei):
                    return False
                
            path.remove(node_idx)
            hashmap[node_idx] = []

            return True

        for i in range(numCourses):    
            if not dfs(i):
                return False
        return True