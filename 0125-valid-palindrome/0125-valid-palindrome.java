class Solution {
    public boolean isPalindrome(String s) {
        String target = "";
        for(int i=0; i<s.length(); i++){
            if(Character.isLetter(s.charAt(i)) || Character.isDigit(s.charAt(i))){
                target += Character.toLowerCase(s.charAt(i));
            }
        }
        
        // System.out.println(target);
        
        if(target.length() == 0){
            return true;
        }

        for(int i=0; i<target.length()/2 + 1; i++){
            if(target.charAt(i) != target.charAt(target.length() - 1 - i)){
                return false;
            }
        }
        return true;
        
    }
}