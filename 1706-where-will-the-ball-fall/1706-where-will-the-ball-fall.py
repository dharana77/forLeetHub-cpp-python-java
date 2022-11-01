class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        answer = list()
        
        for i in range(len(grid[0])):
            current_row = 0
            current_col = i
            
            # print("i", i)
            ln = len(answer)
            
            while current_row < len(grid):
                current_value = grid[current_row][current_col]
                # print("row:", current_row, " col:", current_col, len(grid), current_row)
                if current_col < 0 or current_col >= len(grid[0]):
                    answer.append(-1)
                    # print("added1")
                    break
                
                if current_value == 1:
                    if current_col < len(grid[0]) -1 :
                        if grid[current_row][current_col] == grid[current_row][current_col+1]:
                            current_row += 1
                            current_col += 1
                        else:
                            answer.append(-1)
                            # print("added2")
                            break
                    else:
                        answer.append(-1)
                        # print("added3")
                        break
                elif current_value == -1:
                    if current_col > 0:
                        if grid[current_row][current_col] == grid[current_row][current_col-1]:
                            current_row += 1
                            current_col -= 1
                        else:
                            answer.append(-1)
                            # print("added4")
                            break
                    else:
                        answer.append(-1)
                        # print("added5")
                        break
                
            if ln+1 != len(answer):
                answer.append(current_col)
        
        return answer