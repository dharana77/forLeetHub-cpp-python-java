# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        #
        def get_sum(root, tot):
            tot = root.val
            
            if root.left:
                tot += get_sum(root.left, tot)
            
            if root.right:
                tot += get_sum(root.right, tot)
            return tot
            
        total = get_sum(root, 0)
        # print("total", total_value)
        
        self.mini = float('inf')
        self.maxi = float('-inf')
            
        def helper(root):
            if not root:
                return 0
                
            left = helper(root.left)
            right = helper(root.right)
                
            s = total-(left+right+root.val)
            a = abs((left+right+root.val)-s)
            if a<self.mini and (left+right+root.val)>self.maxi:
                self.mini = a
                self.maxi = left+right+root.val
            return (left+right+root.val)
            
        helper(root)
        return (self.maxi*(total-self.maxi))%((10**9)+7)
    
#         def cal_diff(root):
#             if root.left:
#                 left = get_sum(root.left, 0)
#                 temp = total_value - left
#                 if temp * left > self.answer:
#                     self.answer = temp * left
#                 cal_diff(root.left)
            
#             if root.right:
#                 right = get_sum(root.right, 0)
#                 temp = total_value - right
#                 if temp * right > self.answer:
#                     self.answer = temp * right
#                 cal_diff(root.right)
            
#         cal_diff(root)
            
#         return self.answer % (10**9 + 7)