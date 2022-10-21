class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = list()
        for i, row in enumerate(nums):
            for j, d in enumerate(row):
                if len(result) <= (i + j):
                    result.append(list())
                result[i+j].append(d)
        return [num for i in result for num in reversed(i)]
#         mx_len = 0
#         for i in range(len(nums)):
#             mx_len = max(mx_len, len(nums[i]))
        
#         for i in range(len(nums)):
#             while len(nums[i]) < mx_len:
#                 nums[i].append(0)
            
#         for i in range(len(nums)):
#             j = 0
#             while i>=0 and j <len(nums[0]):
#                 if nums[i][j] != 0 :
#                     ans.append(nums[i][j])
#                 i-=1
#                 j+=1
        
        
#         for j in range(1, len(nums[0])):
#             i = len(nums) - 1
#             while i>=0 and j<len(nums[0]):
#                 if nums[i][j] != 0:
#                     ans.append(nums[i][j])
#                 i-=1
#                 j+=1
    
#         # print(nums)
#         return ans