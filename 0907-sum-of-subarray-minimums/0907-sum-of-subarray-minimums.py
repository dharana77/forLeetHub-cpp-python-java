class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = sum(arr)
        
        mod = 1e9 + 7
        
        st = []
        from_left = [len(arr)] * len(arr)
        for i in range(len(arr)):
            while st and arr[i] <= arr[st[-1]]:
                from_left[st.pop()] = i
            st.append(i)
            # print(st)
       
        from_right = [-1] * len(arr)
        for i in reversed(range(len(arr))):
            while st and arr[st[-1]] > arr[i]:
                from_right[st.pop()] =i
            st.append(i)
        
        # print(from_right)
        
        res = 0
        for idx in range(len(arr)):
            l, r = from_left[idx], from_right[idx]
            res += (r - idx) * (idx -l) * arr[idx]
            res %= mod
            
        return int(res)