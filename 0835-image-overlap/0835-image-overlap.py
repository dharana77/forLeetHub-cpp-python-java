class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ct = collections.Counter()
        for i, row in enumerate(img1):
            for j, col in enumerate(row):
                if col:
                    for i2, row2 in enumerate(img2):
                        for j2, col2 in enumerate(row2):
                            if col2:
                                ct[i - i2, j - j2] += 1
        return max(ct.values() or [0])