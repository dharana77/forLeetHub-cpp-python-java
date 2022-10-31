# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = False
    target = -1
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.target = targetSum
        if root:
            self.inorder(root, 0)
        return self.answer
        
    def inorder(self, root, tot):
        if root:
            tot+=root.val
            
        if root.right is None and root.left is None:
            if tot == self.target:
                self.answer = True
                return 
            
        if root.left:
            # print(root.val)
            self.inorder(root.left, tot)
        if root.right:
            # print(root.val)
            self.inorder(root.right, tot)

        