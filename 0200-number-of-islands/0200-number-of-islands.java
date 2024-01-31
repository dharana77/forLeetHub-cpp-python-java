class Solution {
    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        
        int ans = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j] == '1'){
                    dfs(i, j, grid);
                    ans++;
                }
            }
        }
        return ans;
    }
    
    public void dfs(int i, int j, char[][] grid){
        if(i<0 || i>=grid.length || j< 0 || j>= grid[0].length) return;
        
        if(grid[i][j] == '1'){
    grid[i][j] = '0';
    dfs(i+1, j, grid);
    dfs(i-1, j, grid);
    dfs(i, j+1, grid);
    dfs(i, j-1, grid);
        }
    }
}