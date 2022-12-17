import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> st = new Stack<String>();
        for(int i=0; i<tokens.length; i++){
            if (!tokens[i].equals("+") && !tokens[i].equals("-") && !tokens[i].equals("*") && !tokens[i].equals("/")){
                st.push(tokens[i]);
                // System.out.println(tokens[i]);
            }else{
                int s = Integer.valueOf(st.pop());
                int f = Integer.valueOf(st.pop());
                int res = 0;
                // System.out.println(f +" " + s);
                // System.out.println("test" + tokens[i]);
                if(tokens[i].equals("+")){
                    res = f + s;
                }else if(tokens[i].equals("-")){
                    res = f - s;
                }else if(tokens[i].equals("*")){
                    res = f * s;
                }else if(tokens[i].equals("/")){
                    res = f / s;
                }
                // System.out.println("res" +" " + res);
                st.push(String.valueOf(res));
            }
        }
        // return 1;
        return Integer.valueOf(st.pop());
    }
}