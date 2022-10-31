class Solution:
    result = 0
    
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if int(s[i-1]) >= 1:
                dp[i] += dp[i-1]
            if int(s[i-2:i]) >= 1 and int(s[i-2:i]) <= 26:
                if s[i-2] != "0":
                    # print(i,s[i-1])
                    dp[i] += dp[i-2]
        self.result = dp[len(s)]
        # print("2101")
        # print(dp)
        return self.result