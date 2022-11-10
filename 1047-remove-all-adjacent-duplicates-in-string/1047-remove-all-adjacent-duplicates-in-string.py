class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = []
        
        for i in s:
            if len(st) == 0:
                st.append(i)
            else:
                if st[-1] == i:
                    st.pop()
                else:
                    st.append(i)
                
        ans = "".join(st)
        return ans