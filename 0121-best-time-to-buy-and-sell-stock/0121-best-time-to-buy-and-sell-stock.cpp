#include <stack>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mx = 0;
        stack<int> stack;
        for(int i=0; i<prices.size(); i++){
            if(stack.empty()){
                stack.push(prices[i]);
            }else{
                if(stack.top() > prices[i]){
                    stack.push(prices[i]);
                }else{
                    if(mx < prices[i] - stack.top()){
                        mx = prices[i] - stack.top();
                    }
                }
            }
        }
        return mx;
    }
};