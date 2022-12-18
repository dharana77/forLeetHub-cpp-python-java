import java.util.Stack;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
            Stack<Integer> st = new Stack<Integer>();
            ArrayList<Integer> res = new ArrayList<Integer>();
            int[] ans = new int[temperatures.length];

            for(int i=0; i<temperatures.length; i++){
                if(st.empty()){
                    st.push(i);
                }else{
                    int idx = st.peek();
                    if(temperatures[idx] < temperatures[i]){
                        while(!st.empty() && temperatures[idx] < temperatures[i]){
                            ans[idx] = (i-idx);
                            st.pop();
                            if(st.empty()) break;
                            idx = st.peek();
                        }
                    }
                    st.push(i);
                }
            }
            return ans;
    }
}