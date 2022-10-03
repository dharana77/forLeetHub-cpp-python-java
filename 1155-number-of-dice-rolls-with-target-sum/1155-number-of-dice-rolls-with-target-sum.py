class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (max(k,target)+1) for i in range(n+1)]
        for i in range(1,k+1):
            dp[1][i] = 1
        
        for i in range(2, n+1):
            for j in range(1, target+1):
                t = 1
                while min((k-t), (j-t))>=0:
                    dp[i][j]+=dp[i-1][j-t]
                    t+=1
    
        return dp[n][target]%(10**9 +7)