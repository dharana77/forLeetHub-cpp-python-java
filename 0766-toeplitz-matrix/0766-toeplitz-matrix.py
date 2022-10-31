class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        target = matrix[0][0]
        
        for i in range(len_row - 1):
            col = 0
            row = i
            target = matrix[i][col]
            # print(target)
            while col < len_col and row < len_row:
                if target != matrix[row][col]:
                    return False
                col+=1
                row+=1
        
        for i in range(1, len_col - 1):
            col = i
            row = 0
            target= matrix[row][col]
            # print(target)
            while col < len_col and row < len_row:
                if target != matrix[row][col]:
                    return False
                col+=1
                row+=1
        return True