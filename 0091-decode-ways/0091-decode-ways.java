class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int dp[] = new int[n+1];
        
        dp[0] = 1;
        dp[1] = 1;
        
        if (s.charAt(0) == '0'){
            return 0;
        }
        
        // System.out.println(String.valueOf(s.charAt(0)));
        for(int i=2; i<=n; i++){
            int target = s.charAt(i-1) -'0';
            if (target >=1){
                dp[i] += dp[i-1];
            }
            int age = 10;
            
            String tar = s.substring(i-2, i);
            int target2 = Integer.valueOf(tar);
            
            
            if (target2 >= 10 && target2 <= 26){
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}