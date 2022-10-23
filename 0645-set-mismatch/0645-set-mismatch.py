from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        target = -1
        for i in c:
            if c[i] == 2:
                target = i
        mx = len(nums)
        target2 = -1
        for i in range(1, mx+1):
            if c[i] == 0:
                target2 = i
        
        return [target,target2]