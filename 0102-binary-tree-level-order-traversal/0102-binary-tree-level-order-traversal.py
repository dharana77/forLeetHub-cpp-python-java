# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = list()
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
        self.ans = list()
        startNodes = [root]
        if root == None:
            return self.ans
        
        self.ans.append([root.val])

        while len(startNodes) != 0:
            nextStartNodes = list()
            for startNode in startNodes:
                currentNextNodes = self.visitNodes(startNode)
                for currentNextNode in currentNextNodes:
                    if currentNextNode != None:
                        nextStartNodes.append(currentNextNode)
            if len(nextStartNodes) != 0:
                self.ans.append([node.val for node in nextStartNodes])
            startNodes = nextStartNodes
        
        return self.ans
    
    
    def visitNodes(self, startNode: Optional[TreeNode]):
        res = list()
        if startNode.left != None:
            res.append(startNode.left)
        if startNode.right != None:
            res.append(startNode.right)
        return res
    