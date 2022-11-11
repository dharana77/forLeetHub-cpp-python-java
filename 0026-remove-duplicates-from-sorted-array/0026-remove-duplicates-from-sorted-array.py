class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        nums.sort()
        # print(nums)
        
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                i+=1
                j+=1
        # print(nums)
        return len(nums)