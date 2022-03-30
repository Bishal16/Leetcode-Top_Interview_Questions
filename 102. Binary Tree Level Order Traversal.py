# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return
        q = [root]
        res = []
        while len(q) != 0:            
            root = q[0]
            res.append(root.val)
            if root.left != None:
                q.append(root.left)
            if root.right != None:
                q.append(root.right)
            
            q.pop(0)
        print(res)