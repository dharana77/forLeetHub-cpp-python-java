# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def inorder(root):
            if root.val >= low and root.val <= high:
                self.ans += root.val
            if root.left:
                inorder(root.left)
            if root.right:
                inorder(root.right)
        
        inorder(root)
        return self.ans