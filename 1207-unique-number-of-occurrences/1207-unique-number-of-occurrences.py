class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        ct = defaultdict(int)
        for a in arr:
            ct[a]+=1
        
        unique = defaultdict(bool)
        for a in ct:
            if unique[ct[a]] == False:
                unique[ct[a]] = True
            else:
                return False
        return True