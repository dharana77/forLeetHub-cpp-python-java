class TimeMap:

    def __init__(self):
        self.kt_map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kt_map:
            self.kt_map[key] = []
            
        self.kt_map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kt_map or timestamp < self.kt_map[key][0][0]:
            return "" 
        
        left = 0
        right = len(self.kt_map[key])
        
 
        while left<right:
            mid = (left+right)//2
            if self.kt_map[key][mid][0] <= timestamp: 
                left = mid+1
            else:
                right = mid
        return "" if right == 0 else self.kt_map[key][right-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)