class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        vs = list()
        alphas = dict()
        
        for idx, v in enumerate(s):
            if v in vowels:
                vs.append((idx,v))
            alphas[idx] = v
            
        reversed_vs = sorted(vs, key= lambda x : x[0], reverse=True)
        
        answer = ""
        
        vowels_ct = 0
        for idx, v in enumerate(s):
            temp = s[idx]
            if v in vowels:
                temp = reversed_vs[vowels_ct][1]
                vowels_ct += 1
            
            answer += temp
            
        return answer