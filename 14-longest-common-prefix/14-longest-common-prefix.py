class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        mn = 1e9
        for i in strs:
            if len(i) < mn:
                mn = len(i)
        
        for i in range(0, mn):
            chk = True
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:
                    chk = False
                    break
            if chk:
                answer += temp
            else:
                break
        return answer