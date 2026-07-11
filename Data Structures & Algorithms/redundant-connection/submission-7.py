class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # 2 ---- 1 --- 5
        # |      |
        # |      |
        # 3 ---- 4

        n = len(edges)
        parents = [i for i in range(n+1)] # [0,1,2,3,4,5]
        ranks   = [1] * (n+1)             # [1,1,1,1,1,1]

        def find(n):
            if n != parents[n]: # if this agrees, then it is root
                return find(parents[n]) # keep climbing up till we find the root
                                              # after i climb and find root, 
                                              # i change the path to directly point me to the root next time
            return parents[n]
            
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2: # both give the same root
                return False
            
            if ranks[p1] > ranks[p2]: # make p1 the root
                parents[p2] = p1
                ranks[p1]    += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2]   += ranks[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]