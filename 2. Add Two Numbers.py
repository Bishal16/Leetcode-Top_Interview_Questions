# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c1 = ListNode()
        c1 = ListNode()
        c1=l1
        c2=l2
        carry = 0
        while c1.next!= None and c2.next!= None:
            cv=c1.val
            c1.val = (c1.val + c2.val + carry) % 10 
            carry = int((cv + c2.val + carry )/10)
                
            c1 = c1.next 
            c2 = c2.next
        cv=c1.val
        c1.val = (c1.val + c2.val + carry ) % 10
        carry = int((cv + c2.val + carry )/10)
        if c1.next == None and c2.next == None:
            if carry == 0:
                return l1;
            else:
                last_node = ListNode()
                last_node.val = 1
                c1.next = last_node
                return l1
                
        if c1 != None:   
            c1c = c1
            c1 = c1.next
        if c2 != None:
            c2 = c2.next
        
        if  c1 :
            while c1.next != None:
                cv=c1.val
                c1.val = (c1.val + carry) % 10
                carry = int((cv + carry )/10)
                c1 = c1.next
            cv=c1.val
            c1.val = (c1.val + carry ) % 10
            carry = int((cv + carry )/10)
            
            if carry == 1:
                last_node = ListNode()
                last_node.val = 1
                c1.next = last_node
            return l1
        else:
            c1c.next = c2
            #c1=c1c
            #print(c1c.val)
            #return l1
            c1c = c1c.next
            while c1c.next != None:
                cv = c1c.val
                #print(c1.val)
                c1c.val = (c1c.val + carry) % 10
                #print(c1.val)
                carry = int((cv + carry )/10)
                c1c = c1c.next
            cv=c1c.val
            c1c.val = (c1c.val + carry ) % 10
            carry = int((cv + carry )/10)
            
            if carry == 1:
                last_node = ListNode()
                last_node.val = 1
                c1c.next = last_node
            return l1
        