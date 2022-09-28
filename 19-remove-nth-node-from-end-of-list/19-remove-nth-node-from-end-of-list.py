# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import copy

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ln = 0
        ans = []
        cur = head
        
        while cur:
            ans.append(cur)
            cur = cur.next
            ln+=1
        
        
        if n == ln:
            head = head.next
            return head
        elif n == 1:
            ans[ln-2].next = None
            return head
        else:
            ans[ln-n-1].next = ans[ln-n+1]
        
        return head