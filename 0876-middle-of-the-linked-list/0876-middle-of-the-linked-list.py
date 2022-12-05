# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n+=1
            temp = temp.next
        target = int(n/2)
        ct = 0
        if n==1:
            return head
        while head:
            ct += 1
            head = head.next
            # print(ct,head)
            if ct == target:
                return head