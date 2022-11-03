from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        answer = 0
        others = 0
        
        d = defaultdict(int)
        same = defaultdict(int)
        # print(same, v)
        mx_same = 0
        for word in words:
            if word[0] == word[1]:
                same[word]+=1
                if mx_same < same[word]:
                    mx_same = same[word]
            else:
                reversed_word = word[1] + word[0]
                # print(reversed_word)
                
                if d[reversed_word] >= 1:
                    d[reversed_word]-=1
                    answer+=4
                
                else:
                    d[word] += 1
                    
        if mx_same == 1:
            answer += 2
        else:
            odd = 0
            for key, value in same.items():
                # print(value)
                if value%2 == 1:
                    odd = 1
                    answer += (value-1)*2
                else:
                    answer += (value)*2
            
            answer += 2*odd
        return answer