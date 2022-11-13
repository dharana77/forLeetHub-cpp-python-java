class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        temp = ""
        n = len(lst)
        lst = list(reversed(lst))
        print(lst)
        for i in range(n):
            if lst[i] != " " and lst[i] != "":
                temp += lst[i]
                if i != n - 1:
                    temp += " "
            
        answer = temp
        answer = answer.strip()
        return answer