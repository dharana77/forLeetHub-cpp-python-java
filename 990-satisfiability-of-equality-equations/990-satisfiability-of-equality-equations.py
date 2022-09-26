from collections import defaultdict


class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        
    def find_set(self, x):
        if x != self.set[x]:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]
    
    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x,y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True

    
class Solution:
    def equationsPossible(self, equations):
        union_find = UnionFind(26)
        
        for eq in equations:
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            if eq[1] == "=":
                union_find.union_set(x,y)
        
        for eq in equations:
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            if eq[1] == "!":
                if union_find.find_set(x) == union_find.find_set(y):
                    return False
        return True