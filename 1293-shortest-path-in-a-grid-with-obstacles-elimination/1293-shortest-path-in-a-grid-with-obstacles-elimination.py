from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #return the min number of steps to walk from te upper left corner (0,0) to the lower right corner
        #given that you can eliminate at most k obstacles.
        #it is not possible to find such walk return -1
        
        q = deque()
        q.append((0,0,0,k))
        
        dx = [0,0, 1,-1]
        dy = [1,-1,0,0]
        
        row_len = len(grid)
        col_len = len(grid[0])
        self.ans = 1e9
        
        def bfs(i,j, visited):
            visited[k][i][j] = 1
            
            while q:
                front = q.popleft()
                ci, cj, cv, can = front[0], front[1], front[2], front[3]
                # print(ci,cj,cv,can)
                visited[can][ci][cj] = 1
                
                if ci == row_len - 1 and cj == col_len - 1:
                    if self.ans > cv:
                        self.ans = cv
                        return
                
                for i in range(4):
                    nx, ny = ci+dx[i], cj+dy[i]
                    if nx <0 or nx >= row_len or ny <0 or ny >=col_len:
                        continue
                    
            
                    # print(can, nx,ny)
                    if grid[nx][ny] != 1:
                        nc = deepcopy(can)
                        if visited[nc][nx][ny] != 1:
                            visited[can][nx][ny] = 1
                            q.append((nx,ny,cv+1,nc))
                        # bfs(nx,ny,visited)
                        # visited[nx][ny] = 0
                    elif can > 0 and grid[nx][ny] == 1:
                        nc = deepcopy(can) - 1
                        if visited[nc][nx][ny] != 1:
                            q.append((nx,ny,cv+1, nc))
                            visited[nc][nx][ny] = 1
                        # bfs(nx, ny,visited)
                        # visited[nx][ny] = 0
        
        visited = [[[0] *(col_len) for _ in range(row_len)] for _ in range(k+1)]
        # print(visited)
        # print(visited[0][0][0])
        bfs(0,0,visited)
        
        if self.ans == 1e9:
            self.ans = -1
            
        return self.ans

#[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],
#[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],
#[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],
#[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],
#[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],
#[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],
#[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],
#[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],
#[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],
#[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],
#[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]
#1