from collections import deque

class Solution:
    ans = False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        # m x n grid of cha
        n , m = len(board), len(board[0])
        
        
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        visited = [[False] * m for _ in range(n)]
        
        
        left,right = 1,len(word)-2
        leftDup = rightDup = 1
        
        while left<right:
            if word[left]==word[left-1]:
                leftDup += 1
            if word[right]==word[right+1]:
                rightDup += 1
                
            if rightDup<leftDup:
                word = word[::-1]
                break
                
            if word[left]!=word[left-1]:
                leftDup = 1
            if word[right]!=word[right+1]:
                rightDup = 1
            left += 1
            right -= 1
            
            
        def dfs(x, y, s, visited, k):
            # print(s)
            if s[k] != word[k]:
                return
            
            if s == word:
                # print(s)
                self.ans = True
                return
            
            if len(s) > len(word):
                return
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # print(nx,ny)
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx,ny, s+board[nx][ny], visited, k+1)
                    visited[nx][ny] = False
        
        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                dfs(i,j, board[i][j], visited, 0)
                visited[i][j] = False
                
        return self.ans