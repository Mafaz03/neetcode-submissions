class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nei = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)) :
                pattern = word[ :j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        visited = {beginWord}
        dq = deque([beginWord])

        length = 1
        while dq:
            for i in range(len(dq)):
                word = dq.popleft()
                
                if word == endWord:
                    return length
                
                else:
                    for j in range(len(word)):
                        pattern = word[ :j] + "*" + word[j + 1:]
                        
                        for nei_word in nei[pattern]:
                            if nei_word not in visited:
                                visited.add(nei_word)
                                dq.append(nei_word)
                

            length += 1
        return 0