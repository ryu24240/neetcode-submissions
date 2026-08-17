# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]):

        if node is None and subRoot is None:
            return True

        elif node is None or subRoot is None:
            return False
        
        elif node.val != subRoot.val:
            return False

        else:
            return (self.isSametree(node.right, subRoot.right) and self.isSametree(node.left, subRoot.left))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False

        if self.isSametree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

        


        