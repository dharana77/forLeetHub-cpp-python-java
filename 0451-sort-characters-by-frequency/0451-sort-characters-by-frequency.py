class Solution:
    def frequencySort(self, s: str) -> str:
        #given a string s
        #sort it decreasing order based on the frequency of the charac
        
        ct = {}
        for i in s:
            if i not in ct:
                ct[i] = 1
            else:
                ct[i] += 1
        ct = sorted(ct.items(), key = lambda x : x[1], reverse=True)
        ans = ""
        # print(ct)
        for i in ct:
            for j in range(i[1]):
                ans += i[0]
        
        return ans