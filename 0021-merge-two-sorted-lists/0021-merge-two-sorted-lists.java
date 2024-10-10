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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newList = new ListNode();
        ListNode pt = newList;
        
        while(list1 != null && list2 != null){
            if(list1.val <= list2.val){
                pt.next = list1;
                list1 = list1.next;
            }else{
                pt.next = list2;
                list2 = list2.next;
            }
            pt = pt.next;
        }
        
        if(list1 != null){
            pt.next = list1;
        }else if(list2 != null){
            pt.next = list2;
        }
        return newList.next;
    }
}