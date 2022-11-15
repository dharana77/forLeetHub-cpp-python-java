# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        
        def search(root):
            if not root:
                return
            
            self.answer+=1
            
            if root.left:
                search(root.left)
            
            if root.right:
                search(root.right)
        
        search(root)
        return self.answer