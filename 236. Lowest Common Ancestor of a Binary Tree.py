# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommonAncestor1(root):
            if root == None or root == p or root == q:
                return root          
            left = lowestCommonAncestor1(root.left)    
            right = lowestCommonAncestor1(root.right)       
            if left != None and right!= None:
                print(root.val)
                return root
            elif left!= None:
                return left
            elif right != None:
                return right
            else:
                return None
        return lowestCommonAncestor1(root)