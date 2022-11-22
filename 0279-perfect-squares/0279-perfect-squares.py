from itertools import permutations

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [1e3] * (n + 1)
        for i in range(1, n+1):
            if sqrt(i) == int(sqrt(i)):
                dp[i] = 1
        
        for i in range(1, n+1):
            temp = list()
            tar = int(sqrt(i)) + 1
            # print(i, tar)
            for j in range(1, tar):
                temp.append(j*j)

            for j in temp:
                dp[i] = min(dp[i], dp[i-j] + dp[j])
        # print(dp)
        return dp[n]