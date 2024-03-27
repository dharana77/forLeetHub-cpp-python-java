class Solution {
    public String reverseWords(String s) {
        s = deleteEmptyStringFromStartAndBack(s);
        s = deleteOverSpace(s);
        
        String[] words = new String[s.length()];
        words = s.split(" ");
        
        List<String> answer = new ArrayList<>();
        for(int i=words.length-1; i>=0; i--){
            answer.add(words[i]);
        }
        
        s = String.join(" ", answer);
        return s;
    }
    
    private String deleteOverSpace(String s){
        s = s.replaceAll("\\s+", " ");
        return s;
    }
    
    private String deleteEmptyStringFromStartAndBack(String s){
        int idx = -1;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) != ' '){
                idx = i;
                break;
            }
        }
        s = s.substring(idx, s.length());
        
        int ridx = s.length()-1;
        for(int i=s.length()-1; i>=0; i--){
            if(s.charAt(i) != ' '){
                ridx = i;
                break;
            }
        }
        s = s.substring(0, ridx+1);
        
        return s;
    }
}