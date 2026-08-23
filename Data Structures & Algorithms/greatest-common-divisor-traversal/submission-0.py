class UnionFind:
    def __init__(self, n):
        self.par  = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v):

        while self.par[v] != v:
            self.par[v] = self.par[self.par[v]]
            v = self.par[v]

        return v

    def union(self, v1, v2):

        par1, par2 = self.find(v1), self.find(v2)
        if par1 == par2: return False

        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += self.rank[par2]
        else:
            self.par[par1] = par2
            self.rank[par2] += self.rank[par1]

        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        def prime_factor(n):
            factors = set()

            # pull out 2s
            while n % 2 == 0:
                factors.add(2)
                n = n // 2

            # check with odds
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    factors.add(i)
                    n = n // i

            # if still bigger than 2, itself is prime
            if n > 2:
                factors.add(n)

            return list(factors)

        l = len(nums)
        uf = UnionFind(l)

        factor_hash = {} # prime: index

        for i, n in enumerate(nums):
            for p in prime_factor(n):
                if p in factor_hash:
                    factor_hash[p].append(i)
                    uf.union(factor_hash[p][0], i)

                else:
                    factor_hash[p] = [i]

        return True if max(uf.rank) == l else False
        

        