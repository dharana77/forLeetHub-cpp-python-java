class StockSpanner:

    def __init__(self):
        self.nums = list()
        
    def next(self, price: int) -> int:
        arise = 1
        left = 0
        if len(self.nums) != 0:
            if self.nums[-1][0] <= price:
                arise = self.nums[-1][1] + 1
            
            left = len(self.nums) - 1
            while left != 0 and self.nums[left][0] <= price:
                # print(left, self.nums[left][0])
                left = self.nums[left][2]
        self.nums.append((price,arise, left))
        
        if len(self.nums) == 1:
            return 1
        if left == 0 and self.nums[left][0] <= price:
            return len(self.nums) - left
        else:
            return len(self.nums) - left - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)