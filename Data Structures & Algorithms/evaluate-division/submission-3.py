class Solution:
    def __init__(self):
        self.visited = set()


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        all_var = set()

        self.adj = defaultdict(list) # {a: [b, a/b]}

        for idx, eqn in enumerate(equations):
            a, b = eqn

            all_var.add(a)
            all_var.add(b)

            self.adj[a].append([b, values[idx]])
            self.adj[b].append([a, 1/values[idx]])
        
        res = []

        for ab in queries:
            a = ab[0]
            b = ab[1]


            if (a not in all_var) or (b not in all_var):
                res.append(-1)
            elif (a == b):
                res.append(1)
            else:
                self.visited.clear()
                res.append(self.dfs(a, b))

        return res

        
    def dfs(self, a, b):

        for nxt, val in self.adj[a]:
            if nxt == b:
                return val
        
        res = 1

        for other_nodes in self.adj[a]:

            other_var, other_val = other_nodes

            if other_var not in self.visited:
                self.visited.add(other_var)
                ans = self.dfs(other_var, b)
                if ans != -1:
                    return other_val * ans
                # self.visited.remove(other_var)
        
        return -1

        

        
        