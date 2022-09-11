# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    q = list()
    answer = list()
    level_q = list()
    
    def __init__(self):
        self.q = list()
        self.answer = list()
        self.level_q = list()
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.q = [root]
        binary_tree_list = list()
        if not root:
            return root
        
        while len(self.q) != 0:
            children, parent_val = [], []
            while len(self.q) != 0:
                parent = self.q.pop(0)
                parent_val.append(parent.val)
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            self.q = children
            binary_tree_list.append(parent_val)
        return binary_tree_list
            