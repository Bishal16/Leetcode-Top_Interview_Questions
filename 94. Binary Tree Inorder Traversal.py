# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def _inorderTraversal(self, root: Optional[TreeNode], nodes: List[int]) -> List[int]:
        if root == None :
            return
        self._inorderTraversal(root.left, nodes)
        nodes.append(root.val)
        self._inorderTraversal(root.right, nodes)

    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        nodes = []
        self._inorderTraversal(root, nodes)
        return nodes
    
    