# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def dfs(root):
            if root == None:
                return
            if root.left:
                if root.left.val >= root.val:
                    print('12')
                    self.ans = False
                    
                else:
                    dfs(root.left)
            if root.right:
                if root.right.val <= root.val:
                    print('1')
                    self.ans = False
                    
                else:
                    dfs(root.left)
            return self.ans        
        return dfs(root)