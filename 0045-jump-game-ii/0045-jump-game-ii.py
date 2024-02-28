class Solution:
    def jump(self, nums: List[int]) -> int:
        counting = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if (i + j) >= len(nums):
                    continue
                counting[i+j] = counting[i] + 1 if(counting[i+j] == 0) else min(counting[i]+1, counting[i+j])
                    
        return counting[len(nums)-1]