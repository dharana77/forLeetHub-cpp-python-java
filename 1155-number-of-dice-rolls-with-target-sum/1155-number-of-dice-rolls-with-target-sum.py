class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (max(k,target)+1) for i in range(n+1)]
        for i in range(1,k+1):
            dp[1][i] = 1
        
        for i in range(2, n+1):
            for j in range(1, target+1):
                t = 1
                while t <= min(j,k):
                    dp[i][j]+=dp[i-1][j-t]
                    t+=1
        # 2 2 = 1 11
        # 2 3 = 2 12 21
        # 2 4 = 3 22 13 31
        # 2 5 = 4 14 23 32 41
        # 3 3 = 1 111
        # 3 4 = 3 112 121 211
        # 3 5 =   113 131 311 122 212 221
        return dp[n][target]%(10**9 +7)