class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        preq = [set() for _ in range(numCourses)]

        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        print(graph)
        print(indegree)

        dq = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
        
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    dq.append(v)
                
                preq[v].add(u)
                preq[v] = preq[v].union(preq[u])
        
        res = []
        for a, b in queries:
            res.append(a in preq[b])
        return res    