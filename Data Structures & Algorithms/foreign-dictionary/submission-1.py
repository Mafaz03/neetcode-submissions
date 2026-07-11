class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_hash = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            word_1 = words[i]
            word_2 = words[i+1]

            min_length = min(len(word_1), len(word_2))

            if len(word_1) > len(word_2) and word_1[:min_length] == word_2[:min_length]:
                return ""

            w1 = word_1[:min_length]
            w2 = word_2[:min_length]

            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj_hash[w1[j]].add(w2[j])
                    break

        visited = {} # False: visited | True: visited + in path
        res = []

        def dfs(node):
            if node in visited: # visited or visited + in path
                if visited[node]: 
                    return True # visited + in path = cycle
                else:
                    return False
                
            visited[node] = True # in path
            
            for nei in adj_hash[node]:
                if dfs(nei):
                    return True # cycle is there
                
            visited[node] = False # not in path anymore
            res.append(node)

        for w in adj_hash:
            if dfs(w):
                return ""
        return "".join(res[::-1])
        