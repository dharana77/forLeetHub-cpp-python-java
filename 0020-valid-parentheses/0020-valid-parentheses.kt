import java.util.Stack;

class Solution {
    fun isValid(s: String): Boolean {
        val stack = Stack<Char>();
        
        for(i: Int in 0..s.length-1){
            if(s[i] == '(' || s[i] == '{' || s[i] == '['){
                stack.add(s[i]);
            }else{
                if(stack.size == 0) return false;
                
                if(s[i] == ')'){
                    if(stack.peek() == '(') stack.pop();
                    else return false;
                }
                else if(s[i] == '}'){
                    if(stack.peek() == '{') stack.pop();
                    else return false;
                }
                else if(s[i] == ']'){
                    if (stack.peek() == '[') stack.pop();
                    else return false;
                }
            }
        }
        if(stack.size == 0) return true;
        else return false;
    }
}