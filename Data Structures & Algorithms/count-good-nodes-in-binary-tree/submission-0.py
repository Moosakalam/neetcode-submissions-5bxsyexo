# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,max_so_far):
            if not node :
                return 0 
            is_good = 1 if node.val >= max_so_far else 0

            running_max = max(node.val,max_so_far)

            return is_good + dfs(node.left,running_max) + dfs(node.right,running_max)
        return dfs(root,root.val)