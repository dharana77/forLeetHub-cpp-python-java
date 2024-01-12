# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = int(num1) + int(num2)
        test = res % 10        

        node = ListNode(test, None)
        
        res = (res//10)
        
        ans = node
        
        while res != 0:
            node.next = ListNode(res%10, None)

            res = res // 10
            node = node.next
            
        return ans
        