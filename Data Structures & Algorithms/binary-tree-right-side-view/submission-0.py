# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        que = deque([root])
        while que:
            value_in_level = []
            num_of_nodes = len(que)
            for i in range(num_of_nodes):
                node = que.popleft()
                
                if i == num_of_nodes-1:
                    result.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result