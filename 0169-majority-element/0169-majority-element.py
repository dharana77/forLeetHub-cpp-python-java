from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums).most_common(1)
        print(count)
        
        return count[0][0]