class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        if k >= 2:
            return "".join(sorted(s))
        
        temp = s
        ans = s
        s = s[1:] + s[0]
        if k == 1:
            while temp != s:
                print(s)
                ans = min(ans, s)
                s = s[1:] + s[0]
                
                
        return ans