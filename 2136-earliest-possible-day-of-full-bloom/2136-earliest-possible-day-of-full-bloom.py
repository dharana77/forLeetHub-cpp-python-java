class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        totals = []
        for i, v in enumerate(plantTime):
            totals.append((v,growTime[i]))
        
        totals = sorted(totals, key= lambda x: x[1], reverse= True)
        print(totals)
        
        answer = 0
        current_time = -1
        for tot in totals:
            current_time += tot[0]
            answer = max(answer, current_time + tot[1] + 1)
            print(current_time, answer)
            
        return answer