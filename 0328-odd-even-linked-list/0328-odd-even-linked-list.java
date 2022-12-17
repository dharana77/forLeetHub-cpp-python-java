/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null){
            return head;    
        }
        ListNode odd = head;
        ListNode oddPoint = odd;
        ListNode even = head.next;
        ListNode evenPoint = even;
        
        while (head!= null){
            if(even != null) odd.next = even.next;
            if(odd.next != null) odd = odd.next;
            if(odd != null) even.next = odd.next;
            if(even.next != null) even = even.next;
            if(head.next != null) head = head.next.next;
            else head = head.next;
        }
        if (odd != null) odd.next = evenPoint;
        
        return oddPoint;
    }
}