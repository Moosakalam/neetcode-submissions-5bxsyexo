# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverse(root):
            if not root:
                return None
            root.right , root.left = root.left,root.right 
            inverse(root.right)
            inverse(root.left)
            return root
        return inverse(root) 


        