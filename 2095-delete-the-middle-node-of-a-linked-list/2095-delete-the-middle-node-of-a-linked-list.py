class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        h = 0
        lst = list()
        while temp:
            h+=1
            lst.append(temp)
            temp = temp.next
            
        t = int(h/2)
        
        if h==1:
            return 
        elif h==2:
            lst[0].next = None
            return lst[0]
        
        lst[t-1].next = lst[t+1]
        
        return lst[0]