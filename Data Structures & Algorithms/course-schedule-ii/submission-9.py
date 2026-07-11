class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hashmap = {}
        for idx in range(numCourses):
            hashmap[idx] = []

        for i in prerequisites:
            hashmap[i[0]].append(i[1])
            

        visited = set()
        path_set = set()

        path = []
        def dfs(node):

            
            if node in path_set:
                return False # loop
            
            if node in visited:
                return True # this is the second time we will be coming accross this, then we want to return true
            
            path_set.add(node)

            for nei in hashmap[node]:
                if not dfs(nei):
                    return False
            
            visited.add(node)
            path_set.remove(node)
            
            path.append(node)

            return True

        for i in range(numCourses):
            if dfs(i):
                hashmap[i] = []
            else: 
                return []
        return path



