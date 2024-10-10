import java.util.Stack;

class Solution {
    public int maxProfit(int[] prices) {
        Stack<Integer> st = new Stack<>();
        
        int mx = 0;
        for(int i=0; i<prices.length; i++){
            if(st.isEmpty()){
                st.add(prices[i]);
            }else{
                if(st.peek() > prices[i]){
                    st.add(prices[i]);
                }else{
                    if(mx < prices[i] - st.peek()){
                        mx = prices[i] - st.peek();
                    }            
                }
            }
        }
        return mx;
    }
}