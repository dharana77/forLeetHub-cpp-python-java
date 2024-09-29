class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        #type, color, name 순
        
        ans = 0
        
        for i in range(len(items)):
            target = -1
            if ruleKey == "type":
                target = 0
            elif ruleKey == "color":
                target = 1
            else:
                target = 2
                
            if items[i][target] == ruleValue:
                ans += 1
                
        return ans