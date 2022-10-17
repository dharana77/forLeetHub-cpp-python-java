class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ct = [0] * 28
        
        # print(ord('a'))
        for s in sentence:
            ct[ord(s)-97]+=1
        
        print(ct)
        for i in range(26):
            if ct[i] ==0:
                print(i)
                return False
        return True