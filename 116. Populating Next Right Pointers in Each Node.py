# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         root.next == None
        
#         q = [root]                        
#         while q[0]:
#             node = q[0]
#             if node.left == None : #break while starting the last level
#                 break
            
#             q.append(node.left)
#             node.left.next = node.right 
            
#             q.append(node.right)
#             if node.next != None:
#                 node.right.next = node.next.left                        
            
#             q.pop(0)                    
#         return root
        
# ''' 
        
        
        
        
        
#         q = [root]                
#         vals = []

#         while q[0]:
#             node = q[0]                        
#             q.append(node.left)                        
#             q.append(node.right)                       
            
#             if node.next != None:
#                 x = node.next.val 
#             else:
#                 x=None
#             vals.append(node.val) 
#             print(node.val,'->',x)
#             q.pop(0)
# '''
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q=deque()
        q.append(root)
        while q:
            pivot=None
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    node.next=pivot
                    q.append(node.right)
                    q.append(node.left)
                    pivot=node
        return root