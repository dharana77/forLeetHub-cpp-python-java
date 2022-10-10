class MyCalendarThree:

    def __init__(self):
        self.ct = collections.Counter()
        
    def book(self, start: int, end: int) -> int:
        self.ct[start]+=1
        self.ct[end]-=1
        
        ans = temp = 0
        for c in sorted(self.ct):
            temp+= self.ct[c]
            if temp>ans:
                ans = temp
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)