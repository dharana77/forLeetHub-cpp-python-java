from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        q = deque()
        visited = [0] * (len(bank) + 1)
        answer = 1e9
        
        q.append((start, 0))
        visited = [0] * (len(bank) + 1)
        while q:
            front = q.pop()
            current = front[0]
            ct = front[1]
            # print(current,ct)
            if current == end:
                if answer > ct:
                    answer = ct
                break
            
            
            # print(visited)
            
            for i in range(len(bank)):
                if visited[i] != 1:
                    # print(self.get_diff_count(current, bank[i]))
                    if self.get_diff_count(current, bank[i]) == 1:
                        
                        q.append((bank[i],ct+1))
                        visited[i] = 1
                
        if answer == 1e9:
            answer = -1
            
        return answer
    
                        
    
    def get_diff_count(self, start ,end):
        result = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                result+=1
        return result