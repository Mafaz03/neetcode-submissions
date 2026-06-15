class TreeNode:
    def __init__(self):
        self.children = {}
        self.isLast = False


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word: str):
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TreeNode()
            
            curr = curr.children[w]
        curr.isLast = True

    def search(self, word: str):

        def dfs(idx, root):
            curr = root

            for i in range(idx, len(word)):
                w = word[i]

                if w == ".":
                    for c in curr.children.values():
                        if dfs(i + 1, c):
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
                
            return curr.isLast
        return dfs(0, self.root)

                
            
        