class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        graph_rows = {i: [] for i in range(1, k+1)}
        graph_cols = {i: [] for i in range(1, k+1)}

        for a, b in rowConditions:
            graph_rows[a].append(b)
        
        for a, b in colConditions:
            graph_cols[a].append(b)
    
        path    = set()
        visited_cycle = set()

        def cycleDetect(graph, node):

            visited_cycle.add(node)
            path.add(node)

            for nei in graph[node]:
                if nei in path:
                    return True
                
                if nei not in visited_cycle:
                    if cycleDetect(graph, nei): 
                        return True

            path.remove(node)
            return False
        
        for node in range(1, k+1):
            if node not in visited_cycle:
                if cycleDetect(graph_rows, node):
                    return []
        
        path    = set()
        visited_cycle = set()

        for node in range(1, k+1):
            if node not in visited_cycle:
                if cycleDetect(graph_cols, node):
                    return []

        res = []
        visited = set()

        def dfs(graph, node):
            visited.add(node)


            for nei in graph[node]:
                if nei not in visited:
                    dfs(graph, nei)
            res.append(node)

        for node in graph_rows:
            if node not in visited:
                dfs(graph_rows, node)

        res.reverse()
        res_rows = {res[i]: i for i in range(k)}

        res = []
        visited = set()

        for node in graph_cols:
            if node not in visited:
                dfs(graph_cols, node)

        res.reverse()
        res_cols = {res[i]: i for i in range(k)}

        matrix =  [[0] * k for i in range(k)]
        for i in range(1, k+1):
            matrix[res_rows[i]][res_cols[i]] = i
        return matrix
        