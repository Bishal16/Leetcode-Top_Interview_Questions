# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return root
        l1 , l2 = [], []
        def recursionLefSubtree(root):
            if root:
                l1.append(root.val)
                recursionLefSubtree(root.left)
                recursionLefSubtree(root.right)
            else:
                l1.append(None)
        recursionLefSubtree(root.left)
        # print(l1)
        def recursionRightSubtree(root):
            if root:
                l2.append(root.val)
                recursionRightSubtree(root.right)
                recursionRightSubtree(root.left)
            else:
                l2.append(None)
        recursionRightSubtree(root.right)
        # print(l2)
        if l1 == l2:
            return True
        else:
            return False