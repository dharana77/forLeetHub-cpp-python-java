class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #given an integer array nums and an integer k,
        #return true if nums has at least two whose 
        s = list()
        t = 0
        if len(nums) == 1 and nums[0] == 0:
            return False
        
        m = {0: -1}
        tot = 0
        print(nums)
        for i in range(len(nums)):
            tot+=nums[i]
            tot%=k
            # print(m, tot, tot in m)
            if tot in m:
                if i - m[tot] > 1:
                    return True
            else:
                m[tot] = i
        print(m)
        return False