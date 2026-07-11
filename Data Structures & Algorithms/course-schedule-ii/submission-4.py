class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {}

        for idx in range(numCourses):
            hashmap[idx] = deque([])

        for i in prerequisites:
            hashmap[i[0]].append(i[1])
        

        visited = set()
        path = []

        def dfs(node):
            if node == []:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            
            # print(node)
            
            for nei in hashmap[node]:
                if not dfs(nei):
                    return False
            
            visited.remove(node)
            if node not in path: path.append(node)   
            return True


        for i in range(numCourses):  
            
            if not dfs(i):
                return []


        for i in range(numCourses):
            if i not in path:
                path.append(i)

        return path

    









