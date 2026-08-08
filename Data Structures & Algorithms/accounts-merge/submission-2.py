class unionFind:
    def __init__(self, nodes):
        self.parents = [i for i in range(nodes)]
        self.ranks   = [1] * nodes
    
    def find(self, x):
        if x != self.parents:
            self.parents[x] = self.parents[self.parents[x]] # path compression
            x = self.parents[x]
        return x # returns the root
    
    def union(self, x1, x2):
        par1, par2 = self.find(x1), self.find(x2)
        
        if par1 == par2:
            return False # already in the same group
        
        if self.ranks[par1] > self.ranks[par2]: # par1 is a bigger tree
            self.parents[par2] = par1  # attach smaller tree under the longer tree
            self.ranks[par1] += self.ranks[par2]
        else:
            self.parents[par1] = par2  # attach smaller tree under the longer tree
            self.ranks[par2] += self.ranks[par1]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        union_find = unionFind(len(accounts))
    
        account_idx = {} # {mail: idx}
        for idx, n_m in enumerate(accounts):
            mails = n_m[1:]

            for mail in mails:
                if mail not in account_idx:
                    account_idx[mail] = idx
                else:
                    union_find.union(idx, account_idx[mail]) # join pre-exsisting mail and the
                                                             # new mail that was already used
        
        mail_mails = defaultdict(list) # {leader mail idx: other mails}
        for mail, idx in account_idx.items():
            leader_mail_idx = union_find.find(idx)
            mail_mails[leader_mail_idx].append(mail)
        

        result = []

        for i, mails in mail_mails.items():
            result.append([accounts[i][0]] + sorted(mail_mails[i]))

        return result













