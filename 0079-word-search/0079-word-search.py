from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(board),len(board[0])
        
        # (3) Inverse word if it's better
        # If we find the right duplicates are less than the left duplicates, reverse the word.
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
            
        def backtrack(i,j,k,visited):
            if board[i][j] == word[k]:
                if k==len(word)-1:
                    return True
                for xn,yn in directions:
                    x,y = i+xn,j+yn
                    if 0<=x<m and 0<=y<n and (x,y) not in visited:
                        if backtrack(x,y,k+1,visited.union({(x,y)}))==True:
                            return True
            return False
        
        for i, j in product(range(m), range(n)):
            if backtrack(i,j,0,{(i,j)}):
                return True
        return False