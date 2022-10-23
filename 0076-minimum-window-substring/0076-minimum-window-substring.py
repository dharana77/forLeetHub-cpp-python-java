from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = Counter(t)

        missings = len(t)

        left = start = 0
        end = len(s)
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        if len(t) > len(s):
            return ""

        for right, v in enumerate(s, 1):
            if n[v] > 0:
                missings -= 1
            n[v] -= 1

            if missings == 0:

                if (end - start) > (right - left):
                    end = right
                    start = left

                n[s[left]] += 1
                if n[s[left]] > 0:
                    missings += 1
                left += 1

                while n[s[left]] < 0 and left <= right:
                    n[s[left]] += 1
                    left += 1

                if missings == 0:
                    if (end - start) > (right - left):
                        end = right
                        start = left

        if end == len(s) and start == 0:
            if (Counter(t) & Counter(s)) != Counter(t):
                return ""

        return s[start:end]