from collections import defaultdict

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = sorted(tasks)
        d = defaultdict(int)
        for t in tasks:
            d[t] += 1
        mx_ln = len(tasks)
        dp = [0] * (mx_ln + 1)
        dp[1] = 1e9
        if mx_ln >= 2:
            dp[2] = 1
        if mx_ln >=3 :
            dp[3] = 1
        for i in range(4, mx_ln+1):
            if i>=2: 
                dp[i] = min(dp[i-2], dp[i-3]) + 1
        ans = 0
        # print(d)
        for k, v in d.items():
            # print(k, v, dp[v])
            if dp[v] >= 1e9:
                return -1
            ans += dp[v]
        return ans