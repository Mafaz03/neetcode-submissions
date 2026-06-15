class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast   = False
    
    def add_word(self, root, word: str):
        
        curr = root
        
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        
        curr.isLast = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.add_word(root, w)

        rows = len(board)
        cols = len(board[0])

        words_found = set()

        def backtracking(i, j, node, word):

            if board[i][j] not in node.children:
                return # for that particular (i, j) the trie tree didnt have word
            
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.isLast:
                words_found.add(word)

            ch = board[i][j]
            board[i][j] = "#"

            for (i_off, j_off) in [(0,1), (1,0), (0,-1), (-1,0)]:
                if (0 <= i + i_off < rows) and (0 <= j + j_off < cols):
                    backtracking(i + i_off, j + j_off, node, word)
            
            board[i][j] = ch
        
        for i in range(rows):
            for j in range(cols):
                backtracking(i, j, root, "")
        return list(words_found)





















