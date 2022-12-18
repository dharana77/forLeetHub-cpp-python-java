class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[1001][1001];
        int ln1 = text1.length();
        int ln2 = text2.length();
        for(int i=0; i<=ln1; i++){
            dp[0][i] = 0;
        }
        for(int i=0; i<=ln2; i++){
            dp[i][0] = 0;
        }
        
        for(int i=1; i<=ln1; i++){
            for(int j=1 ;j<=ln2; j++){
                if(text1.charAt(i-1) == (text2.charAt(j-1))){
                    dp[i][j] = dp[i-1][j-1] + 1;
                }else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[ln1][ln2];
    }
}