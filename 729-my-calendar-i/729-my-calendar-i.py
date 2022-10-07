class MyCalendar:
    times = list()
    
    def __init__(self):
        self.times = list()            

    def book(self, start: int, end: int) -> bool:
        times = self.times
        # print(times)
        for time in times:
            # print(time)
            if end <= time[0] or start >= time[1]:
                continue
            return False
        self.times.append((start, end))
        if len(times)==0:
            self.times.append((start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)