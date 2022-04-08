# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        total = 0
        while node:
            total += 1
            node = node.next
        if total == 1:
            return None
        elif total == n:
            return head.next
        total = total - n
        node = head
        x=1
        while x< total:
            node= node.next
            x+=1
        node.next = node.next.next
        return head