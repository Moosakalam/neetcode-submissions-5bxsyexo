# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        
        self.pre_idx = 0
        
        def array_to_tree(in_start, in_end):
            
            if in_start > in_end:
                return None
                
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
          
            mid = inorder_map[root_val]
            
            
            root.left = array_to_tree(in_start, mid - 1)
            root.right = array_to_tree(mid + 1, in_end)
            
            return root
            
        # Kick off the recursion covering the full length of the inorder array
        return array_to_tree(0, len(inorder) - 1)        