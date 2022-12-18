class Solution {
    public int minFallingPathSum(int[][] matrix) {
          int n = matrix[0].length;
            // System.out.println(Integer.MAX_VALUE);
            int[][] arr = new int[n][n];
            for(int i=0; i<n; i++){
                arr[0][i] = matrix[0][i];
            }

            for(int i=1; i<n; i++){
                for(int j=0; j<n; j++){
                    int mn = Integer.MAX_VALUE;
                    if(j-1 >= 0){
                        mn = Math.min(mn, matrix[i][j] + arr[i-1][j-1]);
                    }
                    if(j+1 <n){
                        mn = Math.min(mn, matrix[i][j] + arr[i-1][j+1]);
                    }
                    
                    mn = Math.min(mn, arr[i-1][j] + matrix[i][j]);
                    arr[i][j] = mn;
                }
            }
            int ans = Integer.MAX_VALUE;
            for(int i=0; i<n; i++){
                // System.out.println(arr[n-1][i]);
                if(ans > arr[n-1][i]){
                    ans = arr[n-1][i];
                }
            }
            return ans;
    }
}