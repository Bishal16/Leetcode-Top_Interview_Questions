/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public bool IsPalindrome(ListNode head) {
        var arr = new List<int>();
        ListNode cur  = head;
        while(cur.next != null){
            arr.Add(cur.val);
            cur = cur.next;
        }
        arr.Add(cur.val);
        int i=0, j=arr.Count-1;
        while(i<arr.Count){
            if (arr[i]!=arr[j])
                return false;
         i++;j--;   
        }
        return true;
    }
}