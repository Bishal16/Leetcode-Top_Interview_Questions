# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def recursive(root):
            if root == None:
                return
            
            recursive( root.left )  
            res.append(root.val)
            recursive( root.right )
        recursive(root)
        #res.sort() #for inrder bst its sorted already
        print(res)
        return res[k-1]
        
        