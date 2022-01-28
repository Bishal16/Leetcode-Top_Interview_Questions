# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return head
        nodes = []
        h1=head
        rev = head
        while head.next != None:
            nodes.insert(0, head.val)
            head= head.next
        nodes.insert(0, head.val)
        #print(nodes)
        
        
        h2=h1
        for i in range(len(nodes)):
            h1.val=nodes[i]
            #print(h1.val)
            h1=h1.next
        
        #print(h2)
        return h2