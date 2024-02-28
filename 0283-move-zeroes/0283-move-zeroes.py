class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == 0:
                    next_num = nums[j]
                    temp = next_num
                    nums[j] = 0
                    nums[i] = temp
                    