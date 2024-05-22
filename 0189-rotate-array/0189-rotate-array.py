from copy import deepcopy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = list()
        k %= len(nums)
        res = nums[-k:]
        # print(nums[-1:])
        res += nums[:-k]
        # print(nums)
        # print(res)
        # print(res)
        for i in range(len(nums)):
            nums[i] = res[i]