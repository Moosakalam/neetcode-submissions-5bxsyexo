# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root :
            return False 
        if self.subIsSame(root,subRoot):
            return True
        


        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def subIsSame(self, x, y) -> bool:
        
        if not x and not y:
            return True 
            
       
        if not x or not y:
            return False 
       
        if x.val != y.val:
            return False 
            
        
        return self.subIsSame(x.left, y.left) and self.subIsSame(x.right, y.right)
        