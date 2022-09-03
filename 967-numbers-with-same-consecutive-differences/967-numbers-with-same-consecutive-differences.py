#한국어 번역
#양수가 아닌 n 길이의 정수를 리턴합니다.
#모든 연속적인 두개의 숫자는 k입니다.
#답안에 있는 모든 수는 0으로 시작하지 않아야합니다.
#예를 들어 01은 유효하지않은 0을 가지고 있습니다.
#어떤 순서로도 리턴할 수 있습니다.

# 제한
# 2 <= n <=9 입니다.
# 0 <= k <=9 입니다.

class Solution:
    answer = list()
    
    def add_correct_number(self, n:int, k:int, start:int, items:str):
        # print(items)
        if len(items) == n:
            self.answer.append(items)
            # print(items)
            return
        
        elif len(items) > n:
            return
        
        for i in range(start, 10):
            # print("i:" +str(i))
            if len(items) == 0:
                if start != 0:
                    items+=str(start)
                    self.add_correct_number(n, k, 0, items)
                
            elif abs(int(items[-1]) - i) == k:
                items+=str(i)
                self.add_correct_number(n,k,0,items)
            

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.answer = list()
        for start in range(1,10):
            self.add_correct_number(n, k, start, "")
        
        answer =  sorted(list(set(self.answer)))
        answer = [i for i in answer if len(i) == n]
        return answer
        
        
    
        