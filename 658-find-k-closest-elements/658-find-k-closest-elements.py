class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr = sorted(arr, key=lambda t: abs(t-x))
        print(arr)
        arr = sorted(arr[:k])
        return arr
    