from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #~8:20
        dict_box = defaultdict(list)
        
        for idx, s in enumerate(strs):
            s = sorted(list(sorted(s)))
            st = "".join(s)
            dict_box[st].append(idx)
            
        answer = [[] for _ in range(len(dict_box))]
        
        # print(dict_box)
        # ~45
        ct = 0 
        for key, value in dict_box.items():
            # print(key, value)
            for v in value:
                # print(v)
                answer[ct].append(strs[v])
            ct+=1
        return answer