from itertools import combinations

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = 0
        nums.sort()
        temp = 1e9
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if target == tot:
                    return target
                
                if abs(tot - target) < temp:
                    answer = tot
                    temp = abs(tot - target)
                if tot > target:
                    k-=1
                else:
                    j+=1
        return answer