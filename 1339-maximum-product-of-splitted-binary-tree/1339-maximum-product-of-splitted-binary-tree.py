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
            
        total_value = get_sum(root, 0)
        # print("total", total_value)
        print(total_value)
        
        self.mini = float('inf')
        self.maxi = float('-inf')
        
        def calc_diff(root):
            if not root:
                return 0
            
            left = calc_diff(root.left)
            right = calc_diff(root.right)
            
            tot = total_value - (root.val + left + right)
            # a = abs((left + right + root.val ) - tot)
            if tot * (total_value - tot) > self.maxi:
                self.maxi = tot * (total_value - tot)
                # self.mini = a
            return (left + right + root.val)
        
        calc_diff(root)
        return self.maxi  % (10**9 + 7)