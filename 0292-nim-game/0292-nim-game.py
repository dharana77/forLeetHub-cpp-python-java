class Solution:
    def canWinNim(self, n: int) -> bool:
#         dp = [True, True, True, True, False, True]
#         8 
#         True, True True False, True, True, True, 
#         for i in range(5, n+1):
#             is_appended = False
#             for j in range(3, 1, -1):
#                 # print(dp)
#                 # print(n-j-1)
#                 if dp[n-j] == False:
#                     dp.append(True)
#                     is_appended = True
#                     break
#             if not is_appended:
#                 dp.append(False)
            
#         return dp[n]
        return not n % 4 == 0