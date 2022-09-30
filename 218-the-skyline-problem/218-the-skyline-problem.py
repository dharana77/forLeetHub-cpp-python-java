class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        answer = list()
        temp = list()
        
        if not buildings:
            return list()
        
        height = set()
        
        for building in buildings:
            l,r,h = building
            height.add((l, -h))
            height.add((r, h))
        
        ans, q = [], [0]
        before = q[-1]
        
        for p, h in sorted(height):
            if h < 0:
                insort(q, -h)
            else:
                q.pop(bisect_left(q, h))
            if q[-1] != before:
                ans.append([p, q[-1]])
                before = q[-1]
        return ans