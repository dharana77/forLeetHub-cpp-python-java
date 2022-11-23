class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            temp = board[i]
            nums = [0] * 10
            for j in temp:
                if j == ".":
                    continue
                j = int(j)
                if nums[j] != 0:
                    return False
                nums[j]+=1
        
        for j in range(9):
            nums = [0] * 10
            for i in range(9):
                if board[i][j] == ".":
                    continue
                temp = int(board[i][j])
                if nums[temp] != 0:
                    return False
                nums[temp]+=1
        
        
        targets = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        
        for tar in targets:
            x, y = tar[0], tar[1]
            nums = [0] * 10
            for i in range(3):
                for j in range(3):
                    nx, ny = x+i, y+j
                    temp = board[nx][ny]
                    if temp == ".":
                        continue
                    temp = int(temp)
                    if nums[temp] != 0:
                        return False
                    nums[temp]+=1
                    
        return True