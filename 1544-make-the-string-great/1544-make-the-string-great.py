class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        
        con = True
        while con:
            con = False
            for i, v in enumerate(s):
                # print(i, v)
                if i < len(s) - 1 :
                    if (s[i].isupper() and s[i].lower() == s[i+1]) or (s[i+1].isupper() and s[i+1].lower() == s[i]):
                        s[i] = ""
                        s[i+1] = ""
                        con = True
            s = list("".join(s))
            
        ans = "".join(s)
        return ans