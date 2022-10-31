class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, j = 0, 1
        
        answer = 0
        while i < len(colors) and j < len(colors):
            if i == j:
                j+=1
            if j >= len(colors):
                break
            
            if colors[i] == colors[j]:
                total_idxs = [i]
                mx_idx = i
                mx_value = neededTime[i]
                while j < len(colors) and colors[i] == colors[j]:
                    print(i, j)
                    total_idxs.append(j)
                    if mx_value < neededTime[j]:
                        mx_value = neededTime[j]
                        mx_idx = j
                    j+=1
                print(total_idxs)
                # print(mx_value, mx_idx)
                for k in total_idxs:
                    if k != mx_idx:
                        # print(neededTime[k])
                        answer += neededTime[k]
                
                i=j
            else:
                i+=1
                j+=1
    
        return answer
                