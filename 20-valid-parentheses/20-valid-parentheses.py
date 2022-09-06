class Solution:
    def isValid(self, s: str) -> bool:
        q = list()
        first_count = 0
        second_count = 0
        third_count = 0
        
        for i in s:
            if i=="(":
                first_count+=1
                q.append(i)
                # print(q)
            elif i == "{":
                second_count+=1
                q.append(i)
                # print(q)
            elif i == "[":
                third_count+=1
                q.append(i)
                # print(q)
                # print(first_count, second_count, third_count)
            elif i == ")":
                if first_count > 0 and q[-1] == "(":
                    first_count-=1
                    q = q[:-1]
                    # print(q)
                else:
                    # print(1)
                    return False
                
            elif i == "}":
                if second_count >0 and q[-1] == "{":
                    second_count-=1
                    q = q[:-1]
                    # print(q)
                else:
                    # print(2)
                    return False
            
            elif i == "]":
                if third_count > 0 and q[-1] == "[":
                    third_count-=1
                    q = q[:-1]
                    # print(q)
                else:
                    # print(third_count, q)
                    # print(3)
                    return False
                
        if len(q) == 0:
            return True
        return False
            