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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode answer = new ListNode(0);
        ListNode head = answer;
        
        int nTot = 0;
        while(l1 != null || l2 != null){
            int tot = 0;
            tot += nTot;
            if(l1 != null){
                tot += l1.val;    
            }
            if(l2 != null){
                tot += l2.val;                
            }
            
            if (tot >=10){
                tot -= 10;
                nTot = 1;
            }else{
                nTot = 0;
            }
            answer.val = tot;
            if(l1 != null){
                l1 = l1.next;    
            }
            if(l2 != null){
                l2 = l2.next;    
            }
            
            
            if(l1 != null || l2 != null){
                answer.next = new ListNode(0);    
                answer = answer.next;
            }
        }
        if(nTot == 1){
            answer.next = new ListNode(1);
        }
        return head;
    }
}