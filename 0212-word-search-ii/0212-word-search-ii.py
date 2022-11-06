
class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True
        
    def deleteWord(self, word):
        cur = self
        node_key = list()
        for c in word:
            node_key.append((cur, c))
            cur = cur.children[c]
        
        for parent, child in reversed(node_key):
            target_node = parent.children[child]
            if len(target_node.children) == 0:
                del parent.children[child]
            else:
                return
        
class Solution:

    def findWords(self, board:     list[list[str]], words: list[str]) -> list[str]:
        
        answer = list()
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        row, col = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or r >= row or c <0 or c >= col or
               (r, c) in visited or 
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                answer.append(word)
                node.isWord = False
                trie.deleteWord(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            
            visited.remove((r, c))
        
        for r in range(row):
            for c in range(col):
                dfs(r, c, trie, "")
            
        
        return answer
        