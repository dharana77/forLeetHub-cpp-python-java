class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(list(set(nums))) == len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(1, k+1):
                if i+j > len(nums) -1:
                    continue
                if nums[i] == nums[i+j]:
                    return True
                
        return False
