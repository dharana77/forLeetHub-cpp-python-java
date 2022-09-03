class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for idx, v in enumerate(s):
            if idx -1 >= 0:
                if v == "V" and s[idx-1] == "I":
                    continue
                if v == "X" and s[idx-1] == "I":
                    continue
                
                if v== "L" and s[idx-1] == "X":
                    continue
                if v == "C" and s[idx-1] == "X":
                    continue
                    
                if v == "M" and s[idx-1] == "C":
                    continue
                if v == "D" and s[idx-1] == "C":
                    continue
                
            if idx + 1 < len(s):    
                if v == "I" and s[idx+1] == "V":
                    result += 4
                    continue
                if v == "I" and s[idx+1] == "X":
                    result += 9
                    continue
                    
                if v == "X" and s[idx+1] == "L":
                    result += 40
                    continue
                if v == "X" and s[idx+1] == "C":
                    result += 90
                    continue
                    
                if v == "C" and s[idx+1] == "D":
                    result += 400
                    continue
                if v == "C" and s[idx+1] == "M":
                    result += 900
                    continue
            
            if v == "I":
                result += 1
            elif v =="V":
                result += 5
            elif v == "X":
                result += 10
            elif v == "L":
                result += 50
            elif v == "C":
                result += 100
            elif v == "D":
                result += 500
            elif v == "M":
                result += 1000
            # print(idx, result)
        return result   
    
    "MCMXCIV"