class Solution {
    public boolean detectCapitalUse(String word) {
        boolean up = false;
        boolean low = false;
        
        for(int i=1; i<word.length(); i++){
            int d = word.charAt(i) - 'a';
            int u = word.charAt(i) - 'A';
            if(d>=0 && d<=27){
                low = true;
            }
            if(u>=0 && u<=27){
                up = true;
            }
            // System.out.println(low);
            // System.out.println(up);
            if(up && low){
                return false;
            }
        }
        int d = word.charAt(0) - 'a';
        if(up && (d>=0 && d<=27)){
            return false;
        }
        return true;
    }
}