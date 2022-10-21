from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        d = defaultdict(int)
        for a in arr:
            d[a] += 1
        
        
        d = dict(sorted(d.items(), key = lambda x : x[1]))
        for a in d:
            while d[a]>0 and k>0:
                print(a,d[a],k)
                d[a]-=1
                k-=1
        print(d)
        ans = 0
        for a in d:
            if d[a]>0:
                ans+=1
                
        return ans