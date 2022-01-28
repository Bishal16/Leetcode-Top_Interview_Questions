# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=[]
        a2=[]
        f1=1
        f2=1
        if l1==None:
            f1=0
        else:
            while l1.next!=None:
                a1.append(l1.val)
                l1=l1.next
            a1.append(l1.val)
        if l2==None:
            f2=0
        else:
            while(l2.next!=None):
                a2.append(l2.val)
                l2=l2.next
            a2.append(l2.val)
        
        if f1==0 and f2==0:
            return l1
    
        
        a1=a1+a2
        a1.sort()
        
        
        
        start=ListNode()
        start.val=a1[0]
        start.next=None
        tmp=start
        
        for idx,i in enumerate(a1):
            
            if idx==0:
                continue
            else:
                node=ListNode()
                node.val=i
                node.next=None
                
                tmp.next=node
                tmp=tmp.next

        return start
            