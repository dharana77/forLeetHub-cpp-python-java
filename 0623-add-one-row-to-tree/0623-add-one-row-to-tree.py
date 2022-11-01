
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    target_nodes = list()
      
    def __init__(self):
        self.target_nodes = list()
        
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.get_target_depth_nodes(root, 1, depth)
        
        if len(self.target_nodes) == 0 :
            parent = TreeNode(val, root, None)
            return parent
        
        for tar in self.target_nodes:
            left_temp = tar.left
            right_temp = tar.right
            tar.left = TreeNode(val, left_temp, None)
            tar.right = TreeNode(val, None, right_temp)
        return root
    
    
    def get_target_depth_nodes(self, root, cd, depth):
        if not root:
            return
        
        if cd == depth -1:
            self.target_nodes.append(root)
            return
        
        if root.left:
            self.get_target_depth_nodes(root.left, cd + 1, depth)
        
        if root.right:
            self.get_target_depth_nodes(root.right, cd +1, depth)
        