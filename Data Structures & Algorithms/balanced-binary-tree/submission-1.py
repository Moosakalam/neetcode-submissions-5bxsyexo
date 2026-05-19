# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_depth(node):
            # Base Case: Empty nodes have a depth of 0 and are perfectly balanced
            if not node:
                return 0
                
            # Recursively get the depth of left and right subtrees
            left_depth = check_depth(node.left)
            right_depth = check_depth(node.right)
            
            # If a red flag (-1) was found lower in the tree, keep passing it up
            if left_depth == -1 or right_depth == -1:
                return -1
                
            # If THIS specific node is unbalanced, throw a new red flag
            if abs(left_depth - right_depth) > 1:
                return -1
                
            # If everything is fine, return the actual depth
            return 1 + max(left_depth, right_depth)
            
        # Kick off the recursion. 
        # If the final result is NOT -1, the entire tree is balanced!
        return check_depth(root) != -1
        