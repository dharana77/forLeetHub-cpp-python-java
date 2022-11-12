from bisect import insort


class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        size = len(self.nums)
        if size % 2 == 0:
            return (self.nums[(size-1)//2] + self.nums[size//2]) / 2
        return self.nums[size//2]