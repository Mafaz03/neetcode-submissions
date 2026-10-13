class UnionFind:
    def __init__(self, n):
        self.par  = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v): # returns parent
        while v != self.par[v]:
            self.par[v] = self.par[self.par[v]] # path compression
            v = self.par[v]
        return v

    def union(self, v1, v2): # bool: union possible or already union-fied
        par1, par2 = self.find(v1), self.find(v2)
        if par1 == par2:
            return False
        
        if self.rank[par1] > self.rank[par1]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]
        
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, e in enumerate(edges):
            e.append(i) # [[v1, v2, w, i], ...]

        edges.sort(key = lambda x: x[2]) # sort based on weights

        uf = UnionFind(n)
        min_weight = 0
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                min_weight += w
        print(min_weight)
        c, p = [], []
        # finding critical and pseudo critical edges
        for n1, n2, e_weight, i in edges:

            # critical
            weight = 0
            uf = UnionFind(n)
            edges_count = 0
            for v1, v2, w, j in edges:
                if (i != j) and (uf.union(v1, v2)): # without current edge
                    weight += w
                    edges_count += 1
            
            if (edges_count < n - 1) or (weight > min_weight):
                c.append(i)
                continue

            # pseudo critical
            
            uf = UnionFind(n)
            weight = e_weight
            uf.union(n1, n2)
            for v1, v2, w_j, _ in edges:
                if (uf.union(v1, v2)): # without current edge
                    weight += w_j
            
            if (weight == min_weight):
                p.append(i)

        return [c, p]



            

























